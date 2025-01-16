from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.metrics import f1_score
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
from sklearn.tree import plot_tree
import numpy as np, csv
import matplotlib.pyplot as plt
# import dtreeviz
from dataset import readData

datasetFileName = "dataset-sampled.csv"

X, y, featureNames = readData(datasetFileName)
print(f"Feature names: {featureNames}")
print(f"First 5 feature sets: {X[0:5]}")
print(f"First 5 classes: {y[0:5]}")
print(f"Number of feature sets: {len(X)}")

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
print(f"Feature names: {featureNames}")
print(f"First 5 feature sets: {X[0:5]}")
print(f"First 5 classes: {y[0:5]}")
print(f"Number of feature sets: {len(X)}")

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.5, random_state=0)
clf = xgb.XGBClassifier()

clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = clf.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = clf.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

# skf = StratifiedKFold(n_splits=2)
# scores = cross_val_score(clf, X, y, cv=5)
# print(f"Cross validation score w/ StratifiedKFold: {round(np.mean(scores),3)}")
# 
# sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.5)
# scores = cross_val_score(clf, X, y, cv=sskf)
# print(f"Cross validation score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

