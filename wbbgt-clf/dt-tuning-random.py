from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
import numpy as np, csv, time
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# import dtreeviz

datasetFileName = "dataset-sampled.csv"

def readData(datasetFileName):
    with open(datasetFileName, "r") as f:
        featureNames = []
        X = [] # features
        y = [] # classes
        csvReader = csv.reader(f)
        for rowIndex, row in enumerate(csvReader):
            if rowIndex == 0:
#                 featureNames = [row[0], row[1], row[2], row[3], row[4]]
                featureNames = [row[0], row[1], row[3], row[4]]
            else:
#                 X.append([float(row[0]), float(row[1]),
#                           float(row[2]), float(row[3]), float(row[4])])
                X.append([float(row[0]), float(row[1]),
                          float(row[3]), float(row[4])])
                y.append(int(row[6]))
    return (X, y, featureNames)

X, y, featureNames = readData(datasetFileName)
print(f"Feature names: {featureNames}")
print(f"First 5 feature sets: {X[0:5]}")
print(f"First 5 classes: {y[0:5]}")
print(f"Number of feature sets: {len(X)}")

parameters = {
#               "criterion": ["gini", "entropy", "log_loss"],
#               "max_depth": [None]+[i for i in range(1, 21)],
              "max_depth": list(range(3, 15, 1)),
#               "min_samples_split": [i for i in range(2, 51)],
              "min_samples_split": list(range(4, 50, 2)),
              "min_samples_leaf":  list(range(4, 50, 2)),
              "max_features": ["sqrt", 3, 4],
              "max_leaf_nodes": list(range(2, 20, 2)),
              }

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, random_state=0)
    # 30% (or 20%) for testing, 70% (or 80%) for training
    # Deterministic (non-random) sampling
dTree = DecisionTreeClassifier(random_state=0)

startTime = time.time()

gcv = RandomizedSearchCV(dTree, parameters, n_iter=50000,  cv=5, n_jobs=4)
gcv.fit(X_train, y_train)

optimalModel = gcv.best_estimator_
accuracy = optimalModel.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = optimalModel.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = optimalModel.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")


# accuracy = gcv.score(featuresTesting, classesTesting)
# print (f"Accuracy: {round(accuracy,3)}")

print("Best parameters: ", gcv.best_params_)

skf = StratifiedKFold(n_splits=5)  #K=10分割
scores = cross_val_score(optimalModel, X, y, cv=skf)
print(f"Cross validation score: {round(np.mean(scores),3)}")

sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.3)
scores = cross_val_score(optimalModel, X, y, cv=sskf)
print(f"Cross validation score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

endTime = time.time()
print(f"Exec time: {round(endTime-startTime)} sec, {round((endTime-startTime)/60, 1)} min")

valCombinations = 1
for paramValList in parameters.values():
    valCombinations *= len(paramValList)
print(f"Param val combinations: {valCombinations}")





