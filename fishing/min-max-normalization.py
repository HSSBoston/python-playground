import csv

inputFile = "Tasmania_5years.csv"

with open(inputFile, "r") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    csvHeaderRow = rows[0]
    csvDataRows = rows[1:]
print("Read", inputFile)

