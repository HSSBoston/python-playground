import numpy as np
import pandas as pd
import requests, certifi
from io import StringIO

DATA_URL = "https://kp.gfz.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt"

def fetch_text(url: str) -> str:
    r = requests.get(url, timeout=60, verify=certifi.where())
    r.raise_for_status()
    return r.text

def parse_daily_ap(text: str) -> pd.DataFrame:
    rows = []
    for line in text.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split()  # file is blank-separated ASCII per GFZ format notes
        # First columns are Year, Month, Day (per format description)
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])

        # Ap is present as a daily integer (mean of 8 ap values)
        # In the GFZ format description, Ap appears after 8 ap values. :contentReference[oaicite:3]{index=3}
        # We locate it robustly by reading from the known position in this daily file:
        # After: year month day days days_m bsr db + 8 Kp + 8 ap => Ap
        # That is: 3 + 4 (time fields) + 8 + 8 = 23rd index (0-based 22).
        # If the provider changes spacing, this may need adjustment—print parts length to verify once.
        ap_daily = int(parts[3 + 4 + 8 + 8])  # robust-ish positional parse

        rows.append((pd.Timestamp(y, m, d), ap_daily))

    df = pd.DataFrame(rows, columns=["date", "Ap"]).sort_values("date").reset_index(drop=True)
    return df

def make_quantile_states(x_train: pd.Series, n_states: int = 3):
    # Handle ties via duplicates='drop'
    _, edges = pd.qcut(x_train, q=n_states, retbins=True, duplicates="drop")
    edges = np.unique(edges)
    k = len(edges) - 1
    return edges, k

def assign_states(x: pd.Series, edges: np.ndarray) -> pd.Series:
    # [edge_i, edge_{i+1})
    s = pd.cut(x, bins=edges, labels=False, include_lowest=True, right=False).astype("float")
    s.loc[x == edges[-1]] = (len(edges) - 2)
    return s.astype(int)

def fit_markov(states: np.ndarray, k: int, alpha: float = 0.5) -> np.ndarray:
    counts = np.zeros((k, k), float)
    for a, b in zip(states[:-1], states[1:]):
        counts[a, b] += 1
    counts += alpha
    return counts / counts.sum(axis=1, keepdims=True)

# ---- run ----
text = fetch_text(DATA_URL)
df = parse_daily_ap(text)

# Split example
train = df[(df["date"] >= "1932-01-01") & (df["date"] <= "2009-12-31")]
test  = df[(df["date"] >= "2017-01-01")]

edges, k = make_quantile_states(train["Ap"], n_states=4)
train_states = assign_states(train["Ap"], edges).to_numpy()
P = fit_markov(train_states, k=k, alpha=0.5)

print("Using", k, "states with edges:", edges)
print("Transition matrix:\n", np.round(P, 4))