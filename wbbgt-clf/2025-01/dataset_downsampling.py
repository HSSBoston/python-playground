import csv, random

def downSample(rawDatasetFileName="dataset.csv",
               outputFileName = "dataset-downsampled.csv"):
    print(f"Reading a raw dataset: {rawDatasetFileName}")
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

    with open(rawDatasetFileName, "r") as f:
        csvReader = csv.reader(f)
        for rowIndex, row in enumerate(csvReader):
            if rowIndex == 0:
                csvHeader = row
            else:
                if   row[7] == "0": alertZeroRows.append(row)
                elif row[7] == "1": alertOneRows.append(row)
                elif row[7] == "2": alertTwoRows.append(row)
                elif row[7] == "3": alertThreeRows.append(row)
                elif row[7] == "4": alertFourRows.append(row)

    print("Sample count (alert level 0 to 3): ")
#     print(len(alertZeroRows), len(alertOneRows), len(alertTwoRows),
#           len(alertThreeRows), len(alertFourRows))
    print(len(alertZeroRows), len(alertOneRows), len(alertTwoRows),
          len(alertThreeRows))
    
#     sampleCountList = [len(alertZeroRows), len(alertOneRows), len(alertTwoRows),
#                        len(alertThreeRows), len(alertFourRows)]
    sampleCountList = [len(alertZeroRows), len(alertOneRows), len(alertTwoRows),
                       len(alertThreeRows)]    
    # Excluding sampleCount==0
    minSampleCount = min([sampleCount for sampleCount in sampleCountList
                          if sampleCount !=0])
    print(f"Minimum sample count (excluding 0): {minSampleCount}")

    # random.sample() returns unique samples.
    if len(alertZeroRows) != 0: alertZeroSamples  = random.sample(alertZeroRows,  minSampleCount)
    if len(alertOneRows)  != 0: alertOneSamples   = random.sample(alertOneRows,   minSampleCount)
    if len(alertTwoRows)  != 0: alertTwoSamples   = random.sample(alertTwoRows,   minSampleCount)
    if len(alertThreeRows)!= 0: alertThreeSamples = random.sample(alertThreeRows, minSampleCount)
    if len(alertFourRows) != 0: alertFourSamples  = random.sample(alertFourRows,  minSampleCount) 

    print("Downsampled. Sample count (alert level 0 to 3):")
#     print(len(alertZeroSamples), len(alertOneSamples), len(alertTwoSamples),
#           len(alertThreeSamples), len(alertFourSamples))
    print(len(alertZeroSamples), len(alertOneSamples), len(alertTwoSamples),
          len(alertThreeSamples))
    
#     samples = alertZeroSamples + alertOneSamples + alertTwoSamples + \
#               alertThreeSamples + alertFourSamples
    samples = alertZeroSamples + alertOneSamples + alertTwoSamples + \
              alertThreeSamples

    random.shuffle(samples)

    with open(outputFileName, "w") as f:
        writer = csv.writer(f)
        writer.writerow(csvHeader)
        writer.writerows(samples)

    print(f"Generated {outputFileName}: {len(samples)} rows")

if __name__ == "__main__":
    downSample()
    
    