import csv
import statistics
import matplotlib.pyplot as plt

sizeList = []

with open("constellation-size.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        sizeList.append(float(line[2]))

sizeList.sort(reverse=True)
sizeMax = sizeList[0]
sizeMin = sizeList[-1]
sizeRange = sizeList[0] - sizeList[-1]
sizeMean = statistics.mean(sizeList)
sizeMedian = statistics.median(sizeList)

print("Max:", sizeMax)
print("Min:", sizeMin)
print("Range:", sizeRange)
print("Mean:", round(sizeMean, 3))
print("Median:", round(sizeMedian, 3))

# plt.hist(sizeList, bins=10)

freqs, bins, patches = plt.hist(sizeList, bins=int(sizeRange/70))

modeIndex = freqs.argmax()
sizeMode = bins[modeIndex]
# print(modeIndex)
print("Mode:", round(sizeMode, 3))

plt.xlabel("Constellation Size (sq deg)", size="large")
plt.ylabel("Number of Constellations", size="large")

plt.show()


    