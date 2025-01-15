from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np, csv
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# import dtreeviz

datasetFileName = "dataset.csv"

def readData(datasetFileName):
    with open(datasetFileName, "r") as f:
        featureNames = []
        X = [] # features
        y = [] # classes
        csvReader = csv.reader(f)
        for rowIndex, row in enumerate(csvReader):
            if rowIndex == 0:
                featureNames = [row[0], row[1], row[2], row[3], row[4]]
            else:
                X.append([float(row[0]), float(row[1]),
                          float(row[2]), float(row[3]), float(row[4])])
                y.append(int(row[6]))
    return (X, y, featureNames)

X, y, featureNames = readData(datasetFileName)
print(f"Feature names: {featureNames}")
print(f"First 5 feature sets: {X[0:5]}")
print(f"First 5 classes: {y[0:5]}")
print(f"Number of feature sets: {len(X)}")

parameters = {"criterion": ["gini", "entropy", "log_loss"],
#               "max_depth": [None]+[i for i in range(1, 21)],
              "max_depth": [None, 5, 10, 20, 30, 40, 50],
#               "min_samples_split": [i for i in range(2, 51)],
              "min_samples_split": [2, 5, 10, 20, 30, 40, 50],
              "min_samples_leaf": [1, 5, 10, 20, 30, 40, 50],
              "max_features": [None, "sqrt", "log2"],
#               "max_leaf_nodes": 
              }

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3, random_state=0)
    # 30% (or 20%) for testing, 70% (or 80%) for training
    # Deterministic (non-random) sampling
dTree = DecisionTreeClassifier(random_state=0)

gcv = GridSearchCV(dTree, parameters, cv=10, n_jobs=4)
gcv.fit(X_train, y_train)

optimalModel = gcv.best_estimator_
accuracy = optimalModel.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = optimalModel.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")


# accuracy = gcv.score(featuresTesting, classesTesting)
# print (f"Accuracy: {round(accuracy,3)}")

print("Best parameters: ", gcv.best_params_)

# 
# dTree.fit(featuresTraining, classesTraining)
# accuracy = dTree.score(featuresTesting, classesTesting)
# print (f"Accuracy: {round(accuracy,3)}")
# 
# 
# K分割交差検証
stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(optimalModel, X_test, y_test, cv=stratifiedkfold)
# print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
print(f"Cross validation score: {round(np.mean(scores),3)}")  # スコアの平均値


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
