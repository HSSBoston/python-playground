import csv

inputFile = "Tasmania_5years.csv"

# Optimal temperature: 61–68 °F
# Active Range: 57–72 °F 
optimalLow  = 16.11
optimalHigh = 20
activeLow   = 13.89
activeHigh  = 22.22

tsInOptimal     = 0
tsMaxInOptimal  = 0
tsMinInOptimal = 0

tsInActive    = 0
tsMaxInActive = 0
tsMinInActive = 0

wsInOptimal = 0

with open(inputFile, "r") as f:
    reader = csv.reader(f)
    # Read and ignore the first line/row (header)
    header = next(reader)
    
    # (1)
    for row in reader:
        ts, tsMax, tsMin, ws = float(row[2]), float(row[3]), float(row[4]), float(row[5])

        if optimalLow <= ts <= optimalHigh:
            tsInOptimal += 1
        if ...
        if ...
        if ...
        if ...
        if ...
    
        if 2 <= ws < 4.5:
            wsInOptimal += 1
        
# (2)
allTsInOptimalTotal = tsInOptimal + tsMaxInOptimal + tsMinInOptimal
allTsInActiveTotal  = tsInActive + tsMaxInActive + tsMinInActive
# (3)    
pfsi = ( allTsInOptimalTotal/(21*3) + allTsInActiveTotal/(21*3) * wsInOptimal/21 )/3

