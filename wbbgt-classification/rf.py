from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import numpy as np, csv
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

featureNames = []
features = []
classes = []

with open("dataset09-sampled.csv", "r") as f:
    csvReader = csv.reader(f)
    for rowIndex, row in enumerate(csvReader):
        if rowIndex == 0:
            featureNames = [row[0], row[1], row[2], row[3], row[4]]
        else:
            features.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
            classes.append(int(row[6]))

print(f"Feature names: {featureNames}")
print(f"First 5 feature sets: {features[0:5]}")
print(f"First 5 classes: {classes[0:5]}")


X = features
y = classes

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, random_state=0)
    # 30% for testing, 70% for training
    # Deterministic (non-random) sampling

# dtResults = []
# for depth in range(1, 11):
#     clf = tree.DecisionTreeClassifier(max_depth=depth, random_state=0)
#         # Too shallow tree: poorer classification
#         # Too deep: overfitting
#     clf.fit(X_train, y_train)
#     #     print (f"Depth: {depth}, Accuracy: {round(clf.score(X_test, y_test),3)}")
#     # K分割交差検証
#     stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
#     scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
#     # print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
# #     print(f"Depth: {depth}, Cross validation score: {round(np.mean(scores),3)}")  # スコアの平均値
#     dtResults.append(round(np.mean(scores),3))

clf = RandomForestClassifier(n_estimators=1000, n_jobs=4, random_state=0)
    # n_estimators=100 by default
clf.fit(X_train, y_train)

accuracy = clf.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = clf.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = clf.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

# K分割交差検証
skf = StratifiedKFold(n_splits=5)  #K=10分割
scores = cross_val_score(clf, X, y, cv=skf)
# print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
#     print(f"Depth: {depth}, Cross validation score: {round(np.mean(scores),3)}")  # スコアの平均値
#     rfResults.append(round(np.mean(scores),3))
print(f"Cross validation score: {round(np.mean(scores),3)}")

sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.3)
scores = cross_val_score(clf, X, y, cv=sskf)
print(f"Cross validation score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")



# for i, result in enumerate(dtResults):
#     print(f"Depth: {i+1}, DT: {result}, RF: {rfResults[i]}")


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
