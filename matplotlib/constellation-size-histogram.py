import csv, statistics
import matplotlib.pyplot as plt

sizes = []

with open("constellation-size.csv", "r") as f:
    reader = csv.reader(f)
#    next(reader)
    for row in reader:
        sizes.append(float(row[2]))

sizes.sort(reverse=True)
sizeMax = sizes[0]
sizeMin = sizes[-1]
sizeRange = sizes[0] - sizes[-1]
sizeMean = statistics.mean(sizes)
sizeMedian = statistics.median(sizes)

print("Max:", sizeMax)
print("Min:", sizeMin)
print("Range:", sizeRange)
print("Mean:", round(sizeMean, 3))
print("Median:", round(sizeMedian, 3))

# plt.hist(sizes, bins=88)
freqs, bins, patches = plt.hist(sizes, bins=int(sizeRange/50))

modeIndex = freqs.argmax()
sizeMode = bins[modeIndex]
# print(modeIndex)
print("Mode:", round(sizeMode, 3))

# plt.savefig("rcv-" + today + ".png")
plt.show()
