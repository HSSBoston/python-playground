from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from dataset import readData
import numpy as np, csv, time
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

datasetFileName = "dataset-downsampled.csv"

X, y, featureNames = readData(datasetFileName)
print(f"Feature names: {featureNames}")
print(f"Number of feature sets: {len(X)}")

parameters = {"n_estimators": [2000],
#               "criterion": ["gini", "entropy", "log_loss"],
#               "criterion": ["gini"],
#               "max_depth": [None]+[i for i in range(1, 21)],
              "max_depth": list(range(3, 10, 1)),
#               "min_samples_split": [i for i in range(2, 51)],
              "min_samples_split": list(range(3, 20, 2)),
              "min_samples_leaf":  list(range(2, 20, 2)),
              "max_features": [None, 2, 3, 4, 5],
              "max_leaf_nodes": list(range(2, 50, 2)),
#               "ccp_alpha": np.arange(0, 0.1, 0.001).tolist(),
              }

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=0)

clf = RandomForestClassifier(random_state=0, n_jobs=-1)
skf = StratifiedKFold(n_splits=5)

startTime = time.time()

# Default: cv=5, StratifiedKFold
gcv = GridSearchCV(clf, parameters, cv=skf, n_jobs=-1)
gcv.fit(X, y)

optimalModel = gcv.best_estimator_
accuracy = optimalModel.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = optimalModel.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = optimalModel.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

# cm = confusion_matrix(y_test, y_predicted, labels=[0, 1, 2, 3, 4])
cm = confusion_matrix(y_test, y_predicted, labels=[0, 2, 3, 4])
print(cm)

f1LooseScore = f1_score_loose(cm)
print(f"F1 loose score: {round(f1LooseScore, 3)}")

print("Best parameters: ", gcv.best_params_)

endTime = time.time()
print(f"{round(endTime-startTime)} sec, {round( (endTime-startTime)/60, 1 )} min")

# skf = StratifiedKFold(n_splits=5)  #K=10分割
# scores = cross_val_score(optimalModel, X, y, cv=skf)
# print(f"Cross validation score: {round(np.mean(scores),3)}")
# 
# sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.3)
# scores = cross_val_score(optimalModel, X, y, cv=sskf)
# print(f"Cross validation score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")


