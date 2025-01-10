from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np, dtreeviz, csv
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

featureNames = []
features = []
classes = []

with open("dataset.csv", "r") as f:
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


# X = features
# y = classes

featuresTraining, featuresTesting, classesTraining, classesTesting = train_test_split(features, classes,
                                                                                       test_size=0.3, random_state=0)
    # 30% for testing, 70% for training
    # Deterministic (non-random) sampling
dTree = DecisionTreeClassifier(max_depth=10, random_state=0)
    # Too shallow tree: poorer classification
    # Too deep: overfitting
dTree.fit(featuresTraining, classesTraining)
accuracy = dTree.score(featuresTesting, classesTesting)
print (f"Accuracy: {round(accuracy,3)}")


# K分割交差検証
stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(dTree, features, classes, cv=stratifiedkfold)
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
