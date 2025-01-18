from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.inspection import permutation_importance
import numpy as np, csv
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from dataset import readData

datasetFileName = "dataset-downsampled.csv"

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
                                                    test_size=0.2, random_state=0)
    # 30% for testing, 70% for training
    # Deterministic (non-random) sampling

clf = RandomForestClassifier(n_estimators=2000, random_state=0, n_jobs=-1)
    # n_estimators=100 by default
clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = clf.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = clf.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

skf = StratifiedKFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=skf, scoring="f1_macro")
print(f"Cross validation score: {round(np.mean(scores),3)}")

sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.2)
scores = cross_val_score(clf, X, y, cv=sskf, scoring="f1_macro")
print(f"Cross validation score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

# cm = confusion_matrix(y_test, y_predicted, labels=[0, 1, 2, 3, 4])
cm = confusion_matrix(y_test, y_predicted, labels=[0, 2, 3, 4])
print(cm)

print(clf.feature_importances_)
pImportance = permutation_importance(clf, X, y, n_repeats=100, random_state=0)
print(pImportance["importances_mean"])



# iris = load_iris()
# # print(type(iris))
# X = iris.data   # numpy.ndarray, features
# y = iris.target # numpy.ndarray, species
# print (X[0:5,:])
#     # Sepal Length, Sepal Width, Petal Length, Petal Width
# print(y)
#     # 0: Setosa
#     # 1: Versicolor
#     # 2: Virginica
# print(f"Feature names: {iris.feature_names}")
# print(f"Class names: {iris.target_names}")
# 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#     # 30% for testing, 70% for training
#     # Deterministic (non-random) sampling
# 
# clf = tree.DecisionTreeClassifier(max_depth=3)
#     # Too shallow tree: poorer classification
#     # Too deep: overfitting
# clf.fit(X_train, y_train)
# print ("Accuracy:", clf.score(X_test, y_test))
# 
# print(f"Correct result: {y_test}")
# print(f"Predicted:      {clf.predict(X_test)}")
# 
# # K分割交差検証
# stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
# scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
# # print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
# print(f"Cross validation score: {np.mean(scores)}")  # スコアの平均値
# 
# print( clf.feature_importances_)
# 
# plot_tree(clf,
#           feature_names=iris.feature_names,
#           class_names=iris.target_names,
#           fontsize=10,
#           filled=True)
# plt.show()
# 
# # viz_model = dtreeviz.model(clf,
# #                X_train=X_train,
# #                y_train=y_train,
# #                target_name='Class',
# #                feature_names=iris.feature_names,
# #                class_names=iris.target_names)
# # viz_model.view(scale=0.8)
