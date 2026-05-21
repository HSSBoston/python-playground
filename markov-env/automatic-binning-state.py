"""
Quantile-based (automatic) state binning for USDM DSCI + Markov transition matrix.

- Downloads weekly DSCI for a chosen state and year range from USDM data services.
- Builds quantile-based bins (K states) from TRAINING data only (no leakage).
- Assigns states, prints counts, and estimates a smoothed Markov transition matrix.

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
# 1) Download DSCI
# -----------------------------
USDM_DSCI_STATE_URL = "https://usdmdataservices.unl.edu/api/StateStatistics/GetDSCI"


def _read_csv_https(url: str, timeout_s: int = 60) -> pd.DataFrame:
    r = requests.get(url, timeout=timeout_s, verify=certifi.where())
    r.raise_for_status()
    return pd.read_csv(StringIO(r.text))


def fetch_state_dsci(
    state_fips_2digit: str,
    start_date: str,
    end_date: str,
    statistics_type: int = 1,
) -> pd.DataFrame:
    """
    Fetch DSCI for a state using USDM data service.

    Args:
        state_fips_2digit: e.g., "25" for Massachusetts.
        start_date: "M/D/YYYY" (e.g., "1/1/2011")
        end_date: "M/D/YYYY" (e.g., "12/31/2020")
        statistics_type: keep default 1 unless you know you need something else.

    Returns:
        DataFrame with at least columns including DSCI and a date/week field.
    """
    url = (
        f"{USDM_DSCI_STATE_URL}"
        f"?aoi={state_fips_2digit}"
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
            # Try parse; if it fails, keep as string
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
        """
        Assign states 0..(n_states-1) using stored edges.
        """
        x_clipped = x.clip(lower=self.edges[0], upper=self.edges[-1])
        # right=False => [edge_i, edge_{i+1})
        states = pd.cut(
            x_clipped,
            bins=self.edges,
            labels=False,
            include_lowest=True,
            right=False,
        )
        # Put exact max into last bin (because right=False excludes upper edge)
        states = states.astype("float")
        states.loc[x_clipped == self.edges[-1]] = self.n_states - 1
        return states.astype("int")


def make_quantile_binning(
    x_train: pd.Series,
    n_states: int,
    *,
    clip_range: Tuple[float, float] = (0.0, 500.0),
    min_unique_edges: Optional[int] = None,
) -> QuantileBinning:
    """
    Build quantile bins from training data only.

    Notes:
    - If x has many repeated values (often near 0), quantiles can collide.
      We handle this by using qcut with duplicates='drop'. That may reduce
      the number of bins below n_states. We then (optionally) fall back to fewer states.

    Args:
        x_train: training DSCI values
        n_states: desired number of states (e.g., 5, 7)
        clip_range: DSCI is typically [0, 500]
        min_unique_edges: if provided, enforce at least this many edges; otherwise
                         accept the bins we can form.

    Returns:
        QuantileBinning
    """
    x = x_train.astype(float).clip(*clip_range).dropna()
    if len(x) < 50:
        raise ValueError(f"Too few training samples ({len(x)}) to form quantile bins reliably.")

    # Use qcut to get quantile bin edges robustly.
    # qcut can drop duplicate bins when many identical values exist.
    cats, edges = pd.qcut(x, q=n_states, retbins=True, duplicates="drop")

    # edges is length = actual_bins + 1
    actual_bins = len(edges) - 1
    if actual_bins < n_states:
        print(f"[Info] Requested {n_states} quantile states, but only {actual_bins} could be formed (duplicate edges).")
        if min_unique_edges is not None and len(edges) < min_unique_edges:
            raise ValueError(f"Not enough unique quantile edges: got {len(edges)} edges.")

    # Make edges strictly increasing (numerical safety)
    edges = np.unique(edges)
    actual_bins = len(edges) - 1
    if actual_bins < 2:
        raise ValueError("Quantile binning collapsed to <2 bins. Try fewer states or different training period.")

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

    Args:
        states: integer states 0..n_states-1 in time order
        n_states: number of states
        alpha: smoothing (0.5 is a good default)

    Returns:
        P: (n_states, n_states) transition matrix
    """
    s = states.to_numpy()
    # Remove any NaNs (shouldn't happen if assigned properly)
    s = s[~np.isnan(s)].astype(int)
    if len(s) < 3:
        raise ValueError("Too few state observations to fit transitions.")

    counts = np.zeros((n_states, n_states), dtype=float)
    for a, b in zip(s[:-1], s[1:]):
        if 0 <= a < n_states and 0 <= b < n_states:
            counts[a, b] += 1.0

    # Smooth and normalize rows
    counts_sm = counts + alpha
    row_sums = counts_sm.sum(axis=1, keepdims=True)
    P = counts_sm / row_sums
    return P


# -----------------------------
# 4) End-to-end example: MA 2011–2020 train bins
# -----------------------------
def main():
    # ---- User controls ----
    state_fips = "25"              # Massachusetts
    train_start = "1/1/2011"
    train_end = "12/31/2020"
    n_states_desired = 5
    alpha = 0.5

    # ---- Download ----
    df = fetch_state_dsci(state_fips, train_start, train_end)

    dsci_col = _find_col_case_insensitive(df, "DSCI")
    week = _parse_week_date(df)
    x = df[dsci_col].astype(float)

    week = _parse_week_date(df)
    df = df.assign(_week=week).sort_values("_week").reset_index(drop=True)
    x = df[dsci_col].astype(float)

    # ---- Build quantile bins on training ----
    binning = make_quantile_binning(x, n_states_desired, clip_range=(0.0, 500.0))
    states = binning.assign_states(x)

    # ---- Inspect counts ----
    counts = states.value_counts().sort_index()
    counts.index = [binning.labels[i] for i in counts.index]
    print("\nQuantile-based state counts (training):")
    print(counts)
    print("Total weeks:", int(counts.sum()))

    print("\nQuantile bin edges (DSCI):")
    # edges length = n_states + 1
    for i in range(binning.n_states):
        lo = binning.edges[i]
        hi = binning.edges[i + 1]
        # Show as [lo, hi)
        print(f"{binning.labels[i]}: [{lo:.3f}, {hi:.3f})")

    # ---- Fit transition matrix ----
    P = fit_markov_transition_matrix(states, n_states=binning.n_states, alpha=alpha)

    P_df = pd.DataFrame(P, index=binning.labels, columns=binning.labels)
    print("\nSmoothed transition matrix P (rows sum to 1):")
    print(P_df.round(4))

    # Optional: save binning for reuse on validation/test
    out = {
        "state_fips": state_fips,
        "train_start": train_start,
        "train_end": train_end,
        "n_states_requested": n_states_desired,
        "n_states_actual": binning.n_states,
        "alpha": alpha,
        "edges": binning.edges.tolist(),
        "labels": binning.labels,
    }
    # Save edges/labels so you can apply the same bins to test years (no leakage)
    pd.Series(out).to_json("ma_dsci_quantile_binning.json")
    print("\nSaved binning to ma_dsci_quantile_binning.json")


if __name__ == "__main__":
    main()