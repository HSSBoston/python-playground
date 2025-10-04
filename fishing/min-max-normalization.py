import csv

inputFile = "Tasmania_5years.csv"

def minMaxNormalization(row):
    ts, ws, precip = float(row[2]), float(row[5]), float(row[9])
#     print(yr, doy, ts, ws, precip)
    tsNormalized = 1 - abs(21-ts)/11
    if ws >= 6:
        ws = 6
    wsNormalized = 1 - abs(3-ws)/6
    if precip >= 10:
        precip = 10
    precipNormalized = 1 - precip/10
    return (tsNormalized, wsNormalized, precipNormalized)


with open(inputFile, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
#     rows = [row for row in reader]
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
    
        




