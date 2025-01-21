import csv, numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTEENN

def readRawDataset(rawDatasetFileName):
    with open(rawDatasetFileName, "r") as f:
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

    print(f"Read {rawDatasetFileName}. Total sample count: {len(y)}")
    print("Per-class sample count (alert level 0 to 3):")
    print(perClassSampleCounts(y))
    return (X, y, featureNames)
    
#     if downSampling == "RandomUnderSampler":
#         sampler = RandomUnderSampler(random_state=randomState)
#         X, y = sampler.fit_resample(X, y)
#         print("Downsamping with RandomUnderSampler done.")
#         print("Per-class sample count (alert level 0 to 3):")
#         print(perClassSampleCounts(y))
# 
#     if overSampling == "SMOTE":
#         sampler = SMOTE(random_state=randomState)
#         X, y = sampler.fit_resample(X, y)
#         print("Oversampling with SMOTE done.")
#         print("Per-class sample count (alert level 0 to 3):")
#         print(perClassSampleCounts(y))        
# 
#     if downOverSampling == "SMOTEENN":
#         sampler = SMOTEENN(random_state=randomState, n_jobs=-1)
#         X, y = sampler.fit_resample(X, y)
#         print("Down- and over-samping with SMOTEENN done.")
#         print("Per-class sample count (alert level 0 to 3):")
#         print(perClassSampleCounts(y))
# 
#     if minMaxScaling:
#         scaler = MinMaxScaler()
#             # sampling_strategy="auto": Resampling all calsses but the minority class
#         X = scaler.fit_transform(X)
#         print("Min-max scaling done.")
# 
#     return (X, y, featureNames)

def undersampleRawDataset(inputDatasetFileName,
                          downSampling="RandomUnderSampler",
                          randomState=0,
                          outputFileName="dataset-undersampled.csv"):
    X, y, featureNames = readRawDataset(inputDatasetFileName)
    if downSampling == "RandomUnderSampler":
        sampler = RandomUnderSampler(random_state=randomState)
        X, y = sampler.fit_resample(X, y)
    print(f"Undersampling with {downSampling} done.")
    print("Per-class sample count (alert level 0 to 3):")
    print(perClassSampleCounts(y))
    
    csvRows = []
    for i, x in enumerate(X):
        csvRow = x + [y[i]]
        csvRows.append(csvRow)
    
    with open(outputFileName, "w") as f:
        writer = csv.writer(f)
        writer.writerow(featureNames)
        writer.writerows(csvRows)
    print(f"Generated {outputFileName}: {len(csvRows)} rows \n")
    return (X, y, featureNames)

def OversampleRawDataset(inputDatasetFileName,
                         overSampling="SMOTE",
                         randomState=0,
                         removeTestData=False, # or X_test
                         outputFileName="dataset-oversampled.csv"):
    X, y, featureNames = readRawDataset(inputDatasetFileName)    
    if overSampling == "SMOTE":
        sampler = SMOTE(random_state=randomState)
        X, y = sampler.fit_resample(X, y)
    print(f"Oversampling with {overSampling} done.")
    print("Per-class sample count (alert level 0 to 3):")
    print(perClassSampleCounts(y))
    
    if removeTestData is not False:
        X_test = removeTestData
        removalCount=0
        for i, x in enumerate(X):
            for j, test in enumerate(X_test):
                if np.array_equal(x, test):
                    del X[i]
                    del y[i]
                    removalCount += 1
        print(f"Test data (X_test) removed from the oversampled dataset. Removal count: {removalCount} ")

    csvRows = []
    for i, x in enumerate(X):
        csvRow = x + [y[i]]
        csvRows.append(csvRow)
    
    with open(outputFileName, "w") as f:
        writer = csv.writer(f)
        writer.writerow(featureNames)
        writer.writerows(csvRows)
    print(f" {len(np.unique(X, axis=0))}")
    print(f"Generated {outputFileName}: {len(csvRows)} rows, {len(np.unique(X, axis=0))} unique rows\n")
    return (X, y, featureNames)

def readData(inputDatasetFileName):
    print(f"Reading {inputDatasetFileName}")
    with open(inputDatasetFileName, "r") as f:
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
                y.append(int(row[6]))
    print(f"Total sample count: {len(y)}")
    print("Per-class sample count (alert level 0 to 3):")
    print(perClassSampleCounts(y))
    return (X, y, featureNames)    

def perClassSampleCounts(y):
    return [y.count(0), y.count(1), y.count(2), y.count(3)]


if __name__ == "__main__":
    rawDatasetFileName = "dataset.csv"
    
    print("***** Undersampling")
    X, y, featureNames = undersampleRawDataset(rawDatasetFileName)
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    print("***** Oversampling")
    OversampleRawDataset(rawDatasetFileName)

    print("***** Oversampling, then removing test data (X_test)")
    X_train, y_train, featureNames = OversampleRawDataset(
                                         rawDatasetFileName,
                                         removeTestData = X_test,
                                         outputFileName = "dataset-oversampled-testdata-removed.csv")
    
    
#     X, y, featureNames = readData("dataset.csv")
#     print(f"Feature names: {featureNames}")
#     print(f"First 5 feature sets: {X[0:5]}")
#     print(f"First 5 classes: {y[0:5]}")
#     print(f"Number of feature sets: {len(X)} \n")
#     
#     X, y, featureNames = readData("dataset.csv", downSampling="RandomUnderSampler")
#     print(f"Feature names: {featureNames}")
#     print(f"First 5 feature sets: {X[0:5]}")
#     print(f"First 5 classes: {y[0:5]}")
#     print(f"Number of feature sets: {len(X)} \n")
#    
#     X, y, featureNames = readData("dataset.csv", overSampling="SMOTE")
#     print(f"Feature names: {featureNames}")
#     print(f"First 5 feature sets: {X[0:5]}")
#     print(f"First 5 classes: {y[0:5]}")
#     print(f"Number of feature sets: {len(X)} \n")
# 
#     X, y, featureNames = readData("dataset.csv", downOverSampling="SMOTEENN")
#     print(f"Feature names: {featureNames}")
#     print(f"First 5 feature sets: {X[0:5]}")
#     print(f"First 5 classes: {y[0:5]}")
#     print(f"Number of feature sets: {len(X)} \n")
 