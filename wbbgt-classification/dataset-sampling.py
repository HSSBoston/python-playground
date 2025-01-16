import csv, random

sampleSize = 455
outputFileName = "dataset-sampled.csv"

csvHeader =[]

alertZeroRows  = []
alertOneRows   = []
alertTwoRows   = []
alertThreeRows = []
alertFourRows  = []

alertZeroSamples  = []
alertOneSamples   = []
alertTwoSamples   = []
alertThreeSamples = []
alertFourSamples  = []

with open("dataset.csv", "r") as f:
    csvReader = csv.reader(f)
    for rowIndex, row in enumerate(csvReader):
        if rowIndex == 0:
            csvHeader = row
        else:
            if row[6] == "0":
                alertZeroRows.append(row)
            elif row[6] == "1":
                alertOneRows.append(row)
            elif row[6] == "2":
                alertTwoRows.append(row)
            elif row[6] == "3":
                alertThreeRows.append(row)
            elif row[6] == "4":
                alertFourRows.append(row)

print(len(alertZeroRows), len(alertOneRows), len(alertTwoRows), len(alertThreeRows), len(alertFourRows))

alertZeroSamples  = random.sample(alertZeroRows,  sampleSize)
alertOneSamples   = random.sample(alertOneRows,   sampleSize)
alertTwoSamples   = random.sample(alertTwoRows,   sampleSize)
alertThreeSamples = random.sample(alertThreeRows, sampleSize)
alertFourSamples  = alertFourRows

print(len(alertZeroSamples), len(alertOneSamples), len(alertTwoSamples), len(alertThreeSamples), len(alertFourSamples))

samples = alertZeroSamples + alertOneSamples + alertTwoSamples + alertThreeSamples + alertFourSamples
random.shuffle(samples)

with open(outputFileName, "w") as f:
    writer = csv.writer(f)
    writer.writerow(csvHeader)
    writer.writerows(samples)

print(f"Generated {outputFileName}: {len(samples)} rows")

