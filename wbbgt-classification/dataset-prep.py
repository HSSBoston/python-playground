import os, csv

csvFileNames = os.listdir("csv-files")
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
                if wbgtF > 86.2:
                    classNum = 4
                elif wbgtF > 84.2:
                    classNum = 3
                elif wbgtF > 81.1:
                    classNum = 2
                elif wbgtF > 76.3:
                    classNum = 1
                else:
                    classNum = 0
                newRow = [row[5], row[6], row[7], row[8], row[10], row[9], classNum, alertColors[classNum]]
                csvRows.append(newRow)
    print("Finished reading " + inputFileName)

with open("dataset.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(csvHeader)
    writer.writerows(csvRows)

print(f"Generated dataset.csv: {len(csvRows)} rows")
