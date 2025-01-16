import os, csv

outputFileName = "dataset.csv"

csvFileNames = os.listdir("csv-files")
if os.path.isfile("csv-files/.DS_Store"):
    csvFileNames.remove(".DS_Store")
print(csvFileNames)

alertColors = ["Green", "Yellow", "Orange", "Red", "Black"]
csvHeader = []
csvRows = []

for inputFileName in csvFileNames:
    with open("csv-files/" + inputFileName, "r") as f:
        csvReader = csv.reader(f)
        for rowIndex, row in enumerate(csvReader):
            if rowIndex == 0:
                csvHeader = [row[5], row[6], row[7], row[8], row[10], row[9], "class", "alert color"]
            else:
                wbgtF = float(row[9])
#                 if wbgtF > 86.2:
#                     classNum = 4
#                 elif wbgtF > 84.2:
#                     classNum = 3
#                 elif wbgtF > 81.1:
#                     classNum = 2
#                 elif wbgtF > 76.3:
#                     classNum = 1
#                 else:
#                     classNum = 0
                if wbgtF > 86:
                    classNum = 4
                elif wbgtF > 84:
                    classNum = 3
                elif wbgtF > 81:
                    classNum = 2
                elif wbgtF > 76:
                    classNum = 1
                else:
                    classNum = 0
                newRow = [row[5], row[6], row[7], row[8], row[10], row[9], classNum, alertColors[classNum]]
                csvRows.append(newRow)
    print("Finished reading " + inputFileName)

# Remove duplicated rows
# {(...), (...), ...}
uniqueCsvRowsSet = set([tuple(row) for row in csvRows])
# [[...], [...], ...]
uniqueCsvRows = [list(row) for row in uniqueCsvRowsSet]
print(f"Duplicated rows removed. Before: {len(csvRows)}, After: {len(uniqueCsvRows)}")

with open(outputFileName, "w") as f:
    writer = csv.writer(f)
    writer.writerow(csvHeader)
    writer.writerows(uniqueCsvRows)
print(f"Generated {outputFileName}: {len(uniqueCsvRows)} rows")

alertZeroCount = 0
alertOneCount = 0
alertTwoCount = 0
alertThreeCount = 0
alertFourCount = 0
with open(outputFileName, "r") as f:
    csvReader = csv.reader(f)
    for rowIndex, row in enumerate(csvReader):
        if rowIndex == 0:
            continue
        else:
            if row[6] == "0":
                alertZeroCount += 1
            elif row[6] == "1":
                alertOneCount += 1
            elif row[6] == "2":
                alertTwoCount += 1
            elif row[6] == "3":
                alertThreeCount += 1
            elif row[6] == "4":
                alertFourCount += 1

print(alertZeroCount, alertOneCount, alertTwoCount, alertThreeCount, alertFourCount)

