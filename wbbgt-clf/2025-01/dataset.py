import csv

def readData(datasetFileName):
    with open(datasetFileName, "r") as f:
        featureNames = []
        X = [] # features
        y = [] # classes
        csvReader = csv.reader(f)
        for rowIndex, row in enumerate(csvReader):
            if rowIndex == 0:
                featureNames = [row[0], row[1], row[2], row[3], row[4], row[5]]
#                 featureNames = [row[0], row[1], row[2], row[4], row[5]]
            else:
                X.append([float(row[0]), float(row[1]), float(row[2]), 
                          float(row[3]), float(row[4]), float(row[5])])
#                 X.append([float(row[0]), float(row[1]), float(row[2]),
#                           float(row[4]), float(row[5])])
                y.append(int(row[7]))
    return (X, y, featureNames)

if __name__ == "__main__":
    X, y, featureNames = readData("dataset-sampled.csv")
    print(f"Feature names: {featureNames}")
    print(f"First 5 feature sets: {X[0:5]}")
    print(f"First 5 classes: {y[0:5]}")
    print(f"Number of feature sets: {len(X)}")