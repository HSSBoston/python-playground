import csv

alertZeroCount = 0
alertOneCount = 0
alertTwoCount = 0
alertThreeCount = 0
alertFourCount = 0

with open("dataset.csv", "r") as f:
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