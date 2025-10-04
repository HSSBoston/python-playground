import csv

inputFile = "Tasmania_5years.csv"

with open(inputFile, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
#     rows = [row for row in reader]
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
    
tempMaxNormalized = 1 - abs(21 - tempMaxAvg)/13

if tempDiff > 11:
    tempDiff = 11
tempDiffNormalized = 1- tempDiff/11





