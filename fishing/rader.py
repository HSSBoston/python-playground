import csv, numpy as np, matplotlib.pyplot as plt

inputFile = "Tasmania_5years.csv"

with open(inputFile, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    tempMaxTotal = tempMinTotal = precipTotal = rowCount = 0
    for row in reader:
        tempMax, tempMin, precip = float(row[7]), float(row[8]), float(row[9])
        tempMaxTotal += tempMax
        tempMinTotal += tempMin
        precipTotal += precip
        rowCount += 1
tempMaxAvg = tempMaxTotal/rowCount
tempMinAvg = tempMinTotal/rowCount
tempDiffAvg = tempMaxAvg - tempMinAvg
precipAvg = precipTotal/rowCount
print("Daily avg:", "Max temp", tempMaxAvg, "Temp diff", tempDiffAvg, "Precip", precipAvg)

if tempMaxAvg > 33:
    tempMaxAvg = 33
elif tempMaxAvg < 13:
    tempMaxAvg = 13
tempMaxNormalized = 1 - abs(23 - tempMaxAvg)/11

if tempDiffAvg > 11:
    tempDiffAvg = 11
tempDiffNormalized = 1- tempDiffAvg/11

if precipAvg > 10:
    precipAvg = 10
precipNormarized = 1 - precipAvg/11

print("Normalized:", "Max temp", tempMaxNormalized, "Temp diff", tempDiffNormalized, "Precip", precipNormarized)

categories = ["Temp Diff", "Max Temp", "PFSI", "Precip"]
values = [tempDiffNormalized, tempMaxNormalized, 0.8, precipNormarized]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]
values += values[:1]

fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, linewidth=1, linestyle="solid", label="Tasmania")
ax.fill(angles, values, "blue", alpha=0.1)

# Draw labels
ax.set_thetagrids(np.degrees(angles[:-1]), categories,
                  fontsize=16, fontweight='bold', color="purple")
ax.set_ylim(0, 1)
# ax.set_title("Rader Chart for Fishing Spots")
ax.legend()
plt.show()