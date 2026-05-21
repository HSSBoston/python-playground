import numpy as np
import pandas as pd
import requests, certifi

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

# ---- run ----
text = fetch_text(DATA_URL)
df = parse_daily_ap(text)

# Your proposed fixed bins
edges = [0, 6, 14, 30, np.inf]
labels = ["quiet[0,6)", "unsettled[6,14)", "active[14,30)", "storm[30,+)"]

ap = df["Ap"].astype(float)

states = pd.cut(ap, bins=edges, labels=labels, right=False, include_lowest=True)
counts = states.value_counts().reindex(labels, fill_value=0)

print("State counts:")
print(counts)
print("Total days:", int(counts.sum()))
print("Storm fraction:", float(counts.iloc[-1] / counts.sum()))

# Transition row counts (outgoing transitions)
s = states.astype("category").cat.codes.to_numpy()  # 0..3
row_counts = np.bincount(s[:-1], minlength=4)
print("\nOutgoing transitions per state (row counts):", row_counts)