import csv, numpy as np, matplotlib.pyplot as plt

inputFile = "Tasmania_5years.csv"

def minMaxNormalization(row):
    ts, ws, precip = float(row[2]), float(row[5]), float(row[9])
    tsNormalized = 1 - abs(21-ts)/11
    wsNormalized = 1 - abs(3-ws)/6
    if precip >= 10:
        precip = 10
    precipNormalized = 1 - precip/10
    return (tsNormalized, wsNormalized, precipNormalized)

with open(inputFile, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    tsTotal = wsTotal = precipTotal = rowCount = 0
    for row in reader:
        ts, ws, precip = minMaxNormalization(row)
        tsTotal += ts
        wsTotal += ws
        precipTotal += precip
        rowCount += 1
tsAvg = tsTotal/rowCount
wsAvg = wsTotal/rowCount
precipAvg = precipTotal/rowCount
print(tsAvg, wsAvg, precipAvg)    

categories = ["Temp", "PFSI", "Precip", "Windspeed"]
values = [tsAvg, 0.8, precipAvg, wsAvg]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]
values += values[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, linewidth=1, linestyle="solid", label="Tasmania")
ax.fill(angles, values, "blue", alpha=0.1)

# Draw labels
ax.set_thetagrids(np.degrees(angles[:-1]), categories,
                  fontsize=16, fontweight='bold', color="purple")
ax.set_ylim(0, 1)
# ax.set_title("Rader Chart for Fishing Spots")
ax.legend()
plt.show()