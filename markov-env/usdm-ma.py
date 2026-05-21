import pandas as pd

# --- USDM REST service info ---
# URL structure: https://usdmdataservices.unl.edu/api/[area]/[statistics type]?aoi=...&startdate=...&enddate=...&statisticsType=...
# For states: area = StateStatistics, DSCI = GetDSCI, aoi = 2-digit state FIPS (MA = 25)
# Date format: M/D/YYYY
# (All per USDM Web Service Information page)
BASE = "https://usdmdataservices.unl.edu/api/StateStatistics/GetDSCI"
MA_FIPS = "25"

def fetch_dsci_for_year(year: int) -> pd.DataFrame:
    # Pull one calendar year at a time (safe and simple)
    start = f"1/1/{year}"
    end = f"12/31/{year}"
    url = f"{BASE}?aoi={MA_FIPS}&startdate={start}&enddate={end}&statisticsType=1"
    df = pd.read_csv(url)

    # Common column names seen in USDM outputs include 'Week' and 'DSCI' (case varies).
    # Normalize:
    df.columns = [c.strip() for c in df.columns]
    return df

# --- 1) Download and concatenate 2011–2020 ---
dfs = [fetch_dsci_for_year(y) for y in range(2011, 2021)]
df = pd.concat(dfs, ignore_index=True)

# --- 2) Find the DSCI column robustly ---
dsci_col = None
for c in df.columns:
    if c.lower() == "dsci":
        dsci_col = c
        break
if dsci_col is None:
    raise ValueError(f"Couldn't find DSCI column. Available columns: {df.columns.tolist()}")

# --- 3) Assign 5 fixed-threshold states (edit edges if you want) ---
edges = [0, 5, 20, 100, 200, 500]  # 5 states => 6 edges
labels = ["S0(0-20)", "S1(20-100)", "S2(100-200)", "S3(200-300)", "S4(300-500)"]

# Clamp to [0, 500] just in case
x = df[dsci_col].clip(lower=0, upper=500)

df["state"] = pd.cut(
    x,
    bins=edges,
    labels=labels,
    include_lowest=True,
    right=False  # [0,20), [20,100), ...
)

# Handle the max edge (500) explicitly because right=False excludes 500 from last bin
df.loc[x == 500, "state"] = labels[-1]

# --- 4) Count states ---
state_counts = df["state"].value_counts().reindex(labels, fill_value=0)

print("Weeks in each DSCI state for Massachusetts (2011–2020):")
print(state_counts)
print("\nTotal weeks:", int(state_counts.sum()))