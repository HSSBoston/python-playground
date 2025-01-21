import csv
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTEENN


outputUndersampledFileName = "dataset-undersampled.csv"

def readRawDataset(rawDatasetFileName):
    print(f"Reading {rawDatasetFileName}")
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
    print(f"Total sample count: {len(y)}")
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
                          randomState=0):
    X, y, featureNames = readRawDataset(inputDatasetFileName)
    sampler = RandomUnderSampler(random_state=randomState)
    X, y = sampler.fit_resample(X, y)
    print("Undersampling with RandomUnderSampler done.")
    print("Per-class sample count (alert level 0 to 3):")
    print(perClassSampleCounts(y))
    
    csvRows = []
    for i, x in enumerate(X):
        csvRow = x + [y[i]]
        csvRows.append(csvRow)
    
    with open(outputUndersampledFileName, "w") as f:
        writer = csv.writer(f)
        writer.writerow(featureNames)
        writer.writerows(csvRows)
    print(f"Generated {outputUndersampledFileName}: {len(csvRows)} rows")
    return (X, y)
    
def getData(inputDatasetFileName):
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
    
    undersampleRawDataset(rawDatasetFileName)
    
    
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
 