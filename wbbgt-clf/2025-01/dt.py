from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.inspection import permutation_importance
from wbgt_metrics import f1_score_loose, f1_loose_scorer
import numpy as np, sys
import matplotlib.pyplot as plt
# import dtreeviz
from dataset import readData, perClassSampleCounts
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTEENN

datasetFileName = "dataset.csv"

X, y, featureNames = readData(datasetFileName, minMaxScaling=False, downSampling="RandomUnderSampler")
print(f"Feature names: {featureNames}")
print(f"Number of samples: {len(X)} \n")

print("X, y counts", len(X), len(y))
print("X, y unique counts", len(np.unique(X, axis=0)),
                                      len(np.unique(y, axis=0)))

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=0)

print("X_test, y_test counts", len(X_test), len(y_test))
print("X_test, y_test unique counts", len(np.unique(X_test, axis=0)),
                                      len(np.unique(y_test, axis=0)))

X_train, y_train, featureNames = readData(datasetFileName, minMaxScaling=False, overSampling="SMOTE")

print("X_train, y_train counts", len(X_train), len(y_train))
print("X_train, y_train unique counts", len(np.unique(X_train, axis=0)),
                                      len(np.unique(y_train, axis=0)))

# print(X_test[0])
# print(X_train[0])
# print( np.array_equal(X_test[0], X_train[0]) )

count=0
for i, train in enumerate(X_train):
    for j, test in enumerate(X_test):
        if np.array_equal(train, test):
            del X_train[i]
            del y_train[i]
            count += 1 
print(count, " removed")
print("X_train, y_train counts", len(X_train), len(y_train))
print("X_train, y_train unique counts", len(np.unique(X_train, axis=0)),
                                      len(np.unique(y_train, axis=0)))

print(len(X_train), len(y_train))
print(f"Total sample count for training: {len(y_train)}")
print("Per-class sample count (alert level 0 to 3):")
print(perClassSampleCounts(y_train))        

dTree = DecisionTreeClassifier(random_state=0)
    # Too shallow tree: poorer classification
    # Too deep: overfitting
dTree.fit(X_train, y_train)

accuracy = dTree.score(X_train, y_train)
print (f"Accuracy in training: {round(accuracy,3)}")
accuracy = dTree.score(X_test, y_test)
print (f"Accuracy in testing: {round(accuracy,3)}")

y_predicted = dTree.predict(X_test)
f1score = f1_score(y_test, y_predicted, average="macro")
print(f"F1 score: {round(f1score, 3)}")

# cm = confusion_matrix(y_test, y_predicted, labels=[0, 1, 2, 3, 4])
cm = confusion_matrix(y_test, y_predicted)
print(cm)

f1LooseScore = f1_score_loose(cm)
print(f"F1 loose score: {round(f1LooseScore, 3)}")

# K-fold validation
skf = StratifiedKFold(n_splits=5)
scores = cross_val_score(dTree, X, y, cv=skf, scoring="f1_macro")
print(f"Cross validation F1 score w/ StratifiedKFold: {round(np.mean(scores),3)}")

sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.2)
scores = cross_val_score(dTree, X, y, cv=sskf, scoring="f1_macro")
print(f"Cross validation F1 score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")

scores = cross_val_score(dTree, X, y, cv=skf, scoring=f1_loose_scorer)
print(f"Cross validation F1 loose score w/ StratifiedKFold: {round(np.mean(scores),3)}")

scores = cross_val_score(dTree, X, y, cv=sskf, scoring=f1_loose_scorer)
print(f"Cross validation F1 loose score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")


print(dTree.feature_importances_)
pImportance = permutation_importance(dTree, X, y, n_repeats=100, random_state=0)
print(pImportance["importances_mean"])


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
