import csv, statistics

inputFile = "Tasmania5years.csv"

# Optimal temperature: 61–68 °F
# Active Range: 57–72 °F
optimalLow  = 21.11
optimalHigh = 25
activeLow   = 18.89
activeHigh  = 27.22

pfsiList = []
# (1)
for year in range(2021, 2026):
    tsInOptimal     = 0
    tsMaxInOptimal  = 0
    tsMinInOptimal = 0
    tsInActive    = 0
    tsMaxInActive = 0
    tsMinInActive = 0
    wsInOptimal = 0
    allTsInOptimalTotal = 0
    allTsInActiveTotal = 0
    pfsi = 0

    with open(inputFile, "r") as f:
        reader = csv.reader(f)
        # Read and ignore the first line/row (header)
        header = next(reader)

        for row in reader:
            yr = int(row[0])
            if year == yr:
               ts, tsMax, tsMin, ws = float(row[2]), float(row[3]), float(row[4]), float(row[6])

               if optimalLow <= ts <= optimalHigh:
                   tsInOptimal += 1
               if activeLow <= ts <= activeHigh:
                   tsInActive += 1
               if optimalLow <= tsMax <= optimalHigh:
                   tsMaxInOptimal += 1
               if activeLow <= tsMax <= activeHigh:
                   tsMaxInActive += 1
               if optimalLow <= tsMin <= optimalHigh:
                   tsMinInOptimal += 1
               if activeLow <= tsMin <= activeHigh:
                   tsMinInActive += 1
               if 2.0 <= ws < 4.5:
                   wsInOptimal += 1
#                    print(year, ws)
#             print(year)

# (2)
        allTsInOptimalTotal = tsInOptimal + tsMaxInOptimal + tsMinInOptimal
        allTsInActiveTotal  = tsInActive + tsMaxInActive + tsMinInActive
        print (allTsInOptimalTotal)
        print (allTsInActiveTotal)
        print(wsInOptimal)
# (3)
        print(allTsInOptimalTotal/(21*3))
        print(allTsInActiveTotal/(21*3))
        print(wsInOptimal)
        pfsi = ( allTsInOptimalTotal/(21*3) + allTsInActiveTotal/(21*3) + wsInOptimal/21 )/3
        print (pfsi)
        pfsiList.append(pfsi)

print("Avg PFSI:", statistics.mean(pfsiList))

outputFileName = inputFile + "-pfsi.csv"
with open(outputFileName, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["YEAR", "PFSI"])
    year = 2021
    for i in range(0, 5):
        writer.writerow([year, pfsiList[i]])
        year += 1
        