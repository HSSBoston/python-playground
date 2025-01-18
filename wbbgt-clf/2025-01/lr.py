from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.inspection import permutation_importance
from sklearn.tree import plot_tree
from wbgt_metrics import f1_score_loose, f1_loose_scorer
import numpy as np
from dataset import readData

datasetFileName = "dataset-downsampled.csv"

X, y, featureNames = readData(datasetFileName)
print(f"Feature names: {featureNames}")
print(f"Number of feature sets: {len(X)}")

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=0)
lr = LogisticRegression(max_iter=100, random_state=0)
lr.fit(X_train, y_train)

accuracy = lr.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = lr.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = lr.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

# cm = confusion_matrix(y_test, y_predicted, labels=[0, 1, 2, 3, 4])
cm = confusion_matrix(y_test, y_predicted, labels=[0, 2, 3, 4])
print(cm)

f1LooseScore = f1_score_loose(cm)
print(f"F1 loose score: {round(f1LooseScore, 3)}")

# K-fold validation
skf = StratifiedKFold(n_splits=5)
scores = cross_val_score(lr, X, y, cv=skf, scoring="f1_macro")
print(f"Cross validation F1 score w/ StratifiedKFold: {round(np.mean(scores),3)}")

sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.2)
scores = cross_val_score(lr, X, y, cv=sskf, scoring="f1_macro")
print(f"Cross validation F1 score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

scores = cross_val_score(lr, X, y, cv=skf, scoring=f1_loose_scorer)
print(f"Cross validation F1 loose score w/ StratifiedKFold: {round(np.mean(scores),3)}")

scores = cross_val_score(lr, X, y, cv=sskf, scoring=f1_loose_scorer)
print(f"Cross validation F1 loose score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

# print(svc.feature_importances_)
# pImportance = permutation_importance(svc, X, y, n_repeats=100, random_state=0)
# print(pImportance["importances_mean"])




