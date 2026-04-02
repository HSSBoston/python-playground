"""
Quantile-based (automatic) state binning for USDM DSCI + Markov transition matrix (COUNTY version).

- Downloads weekly DSCI for a chosen COUNTY (5-digit FIPS) and year range from USDM data services.
- Builds quantile-based bins (K states) from TRAINING data only (no leakage).
- Assigns states, prints counts, and estimates a smoothed Markov transition matrix.

USDM REST URL format and AOI rules:
https://usdmdataservices.unl.edu/api/[area]/[statistics type]?aoi=...&startdate=...&enddate=...&statisticsType=...
- area for counties: CountyStatistics
- statistics type for DSCI: GetDSCI
- aoi for counties: 5-digit county FIPS (or 2-letter state abbreviation to get all counties in that state)
Source: USDM Web Service Info. :contentReference[oaicite:2]{index=2}

Works around macOS SSL issues by using requests + certifi.
"""

from __future__ import annotations

from dataclasses import dataclass
from io import StringIO
from typing import Tuple, Optional, List

import numpy as np
import pandas as pd
import requests
import certifi


# -----------------------------
# 1) Download DSCI (County)
# -----------------------------
USDM_DSCI_COUNTY_URL = "https://usdmdataservices.unl.edu/api/CountyStatistics/GetDSCI"


def _read_csv_https(url: str, timeout_s: int = 60) -> pd.DataFrame:
    r = requests.get(url, timeout=timeout_s, verify=certifi.where())
    r.raise_for_status()
    return pd.read_csv(StringIO(r.text))


def fetch_county_dsci(
    county_fips_5digit: str,
    start_date: str,
    end_date: str,
    statistics_type: int = 1,
) -> pd.DataFrame:
    """
    Fetch DSCI for a county using USDM data service.

    Args:
        county_fips_5digit: e.g., "25017" for Middlesex County, MA.
        start_date: "M/D/YYYY" (e.g., "1/1/2011")
        end_date: "M/D/YYYY" (e.g., "12/31/2020")
        statistics_type: 1=traditional, 2=categorical (per USDM docs). :contentReference[oaicite:3]{index=3}

    Returns:
        DataFrame with at least columns including DSCI and a date/week field.
    """
    if not (isinstance(county_fips_5digit, str) and len(county_fips_5digit) == 5 and county_fips_5digit.isdigit()):
        raise ValueError("county_fips_5digit must be a 5-digit string, e.g. '25017'.")

    url = (
        f"{USDM_DSCI_COUNTY_URL}"
        f"?aoi={county_fips_5digit}"
        f"&startdate={start_date}"
        f"&enddate={end_date}"
        f"&statisticsType={statistics_type}"
    )
    df = _read_csv_https(url)
    df.columns = [c.strip() for c in df.columns]
    return df


def fetch_all_counties_in_state_dsci(
    state_abbrev_2letter: str,
    start_date: str,
    end_date: str,
    statistics_type: int = 1,
) -> pd.DataFrame:
    """
    Optional: Fetch DSCI for ALL counties in a state in one call by passing the 2-letter
    state abbreviation as AOI (supported for counties per USDM docs). :contentReference[oaicite:4]{index=4}

    Example: state_abbrev_2letter="MA"
    """
    if not (isinstance(state_abbrev_2letter, str) and len(state_abbrev_2letter) == 2 and state_abbrev_2letter.isalpha()):
        raise ValueError("state_abbrev_2letter must be a 2-letter string, e.g. 'MA'.")

    url = (
        f"{USDM_DSCI_COUNTY_URL}"
        f"?aoi={state_abbrev_2letter.upper()}"
        f"&startdate={start_date}"
        f"&enddate={end_date}"
        f"&statisticsType={statistics_type}"
    )
    df = _read_csv_https(url)
    df.columns = [c.strip() for c in df.columns]
    return df


def _find_col_case_insensitive(df: pd.DataFrame, target: str) -> str:
    for c in df.columns:
        if c.strip().lower() == target.lower():
            return c
    raise ValueError(f"Could not find column '{target}'. Available columns: {df.columns.tolist()}")


def _parse_week_date(df: pd.DataFrame) -> pd.Series:
    """
    USDM CSVs can have different date-like columns depending on endpoint versions.
    Try a few common ones. If none found, return a simple integer index.
    """
    candidates = ["Week", "ValidStart", "ValidEnd", "Date", "MapDate"]
    for name in candidates:
        if any(c.strip().lower() == name.lower() for c in df.columns):
            col = _find_col_case_insensitive(df, name)
            s = pd.to_datetime(df[col], errors="coerce")
            if s.notna().any():
                return s
            return df[col].astype(str)
    return pd.Series(np.arange(len(df)), name="idx")


# -----------------------------
# 2) Quantile binning
# -----------------------------
@dataclass(frozen=True)
class QuantileBinning:
    n_states: int
    edges: np.ndarray          # length = n_states + 1
    labels: List[str]          # length = n_states

    def assign_states(self, x: pd.Series) -> pd.Series:
        x_clipped = x.clip(lower=self.edges[0], upper=self.edges[-1])

        states = pd.cut(
            x_clipped,
            bins=self.edges,
            labels=False,
            include_lowest=True,
            right=False,  # [edge_i, edge_{i+1})
        )

        states = states.astype("float")
        states.loc[x_clipped == self.edges[-1]] = self.n_states - 1
        return states.astype("int")


def make_quantile_binning(
    x_train: pd.Series,
    n_states: int,
    *,
    clip_range: Tuple[float, float] = (0.0, 500.0),
) -> QuantileBinning:
    """
    Build quantile bins from training data only.
    Handles duplicate quantile edges via duplicates='drop'.
    """
    x = x_train.astype(float).clip(*clip_range).dropna()
    if len(x) < 50:
        raise ValueError(f"Too few training samples ({len(x)}) to form quantile bins reliably.")

    _, edges = pd.qcut(x, q=n_states, retbins=True, duplicates="drop")
    edges = np.unique(edges)  # numerical safety

    actual_bins = len(edges) - 1
    if actual_bins < n_states:
        print(f"[Info] Requested {n_states} quantile states, but only {actual_bins} could be formed (duplicate edges).")

    if actual_bins < 2:
        raise ValueError("Quantile binning collapsed to <2 bins. Try fewer states or a different training period.")

    labels = [f"S{i}" for i in range(actual_bins)]
    return QuantileBinning(n_states=actual_bins, edges=edges, labels=labels)


# -----------------------------
# 3) Markov transition matrix (smoothed)
# -----------------------------
def fit_markov_transition_matrix(
    states: pd.Series,
    n_states: int,
    alpha: float = 0.5,
) -> np.ndarray:
    """
    Fit a single transition matrix P where P[i,j] = P(S_{t+1}=j | S_t=i).
    Uses Laplace/Dirichlet smoothing with parameter alpha.
    """
    s = states.to_numpy()
    s = s[~np.isnan(s)].astype(int)

    if len(s) < 3:
        raise ValueError("Too few state observations to fit transitions.")

    counts = np.zeros((n_states, n_states), dtype=float)
    for a, b in zip(s[:-1], s[1:]):
        if 0 <= a < n_states and 0 <= b < n_states:
            counts[a, b] += 1.0

    counts_sm = counts + alpha
    P = counts_sm / counts_sm.sum(axis=1, keepdims=True)
    return P


# -----------------------------
# 4) End-to-end example: County DSCI, 2011–2020
# -----------------------------
def main():
    # ---- User controls ----
    county_fips = "25017"          # Example: Middlesex County, MA (replace with your county)
    train_start = "1/1/2011"
    train_end = "12/31/2020"
    n_states_desired = 5
    alpha = 0.5

    # ---- Download ----
    df = fetch_county_dsci(county_fips, train_start, train_end)

    dsci_col = _find_col_case_insensitive(df, "DSCI")

    # Sort by week/date to ensure correct transitions
    week = _parse_week_date(df)
    df = df.assign(_week=week).sort_values("_week").reset_index(drop=True)

    x = df[dsci_col].astype(float)

    # ---- Build quantile bins on training ----
    binning = make_quantile_binning(x, n_states_desired, clip_range=(0.0, 500.0))
    states = binning.assign_states(x)

    # ---- Inspect counts ----
    counts = states.value_counts().sort_index()
    counts.index = [binning.labels[i] for i in counts.index]
    print(f"\nQuantile-based state counts (training) for county FIPS {county_fips}:")
    print(counts)
    print("Total weeks:", int(counts.sum()))

    print("\nQuantile bin edges (DSCI):")
    for i in range(binning.n_states):
        lo = binning.edges[i]
        hi = binning.edges[i + 1]
        print(f"{binning.labels[i]}: [{lo:.3f}, {hi:.3f})")

    # ---- Fit transition matrix ----
    P = fit_markov_transition_matrix(states, n_states=binning.n_states, alpha=alpha)
    P_df = pd.DataFrame(P, index=binning.labels, columns=binning.labels)
    print("\nSmoothed transition matrix P (rows sum to 1):")
    print(P_df.round(4))

    # Save binning for reuse on validation/test (no leakage)
    out = {
        "county_fips": county_fips,
        "train_start": train_start,
        "train_end": train_end,
        "n_states_requested": n_states_desired,
        "n_states_actual": binning.n_states,
        "alpha": alpha,
        "edges": binning.edges.tolist(),
        "labels": binning.labels,
    }
    out_path = f"county_{county_fips}_dsci_quantile_binning.json"
    pd.Series(out).to_json(out_path)
    print(f"\nSaved binning to {out_path}")


if __name__ == "__main__":
    main()