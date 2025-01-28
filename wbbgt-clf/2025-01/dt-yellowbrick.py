from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, StratifiedKFold, cross_val_score
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.inspection import permutation_importance
from wbgt_metrics import f1_score_loose, f1_loose_scorer
import numpy as np, sys
import matplotlib.pyplot as plt
# import dtreeviz
from dataset_prep import undersample, oversample
from yellowbrick.model_selection import validation_curve

rawDatasetFileName = "dataset.csv"
X, y, featureNames = undersample(rawDatasetFileName)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=0)

X_train, y_train, featureNames = oversample(rawDatasetFileName,
                                            overSampling="SMOTE", # or SMOTEENN
                                            removeTestData = X_test)
X = np.concatenate([X_train, X_test])
y = np.concatenate([y_train, y_test])

skf = StratifiedKFold(n_splits=5)
sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.2)

# fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.add_subplot()
# plt.xticks(range(1, 20, 1))
visualizer = validation_curve(DecisionTreeClassifier(random_state=0),
                              X,
                              y,
                              param_name = "max_depth", param_range = range(1, 21),
#                               param_name = "max_leaf_nodes", param_range = range(2, 201),
#                               param_name = "min_samples_split", param_range = range(2, 101, 2), #def 2
#                               param_name = "min_samples_leaf", param_range = range(1, 101, 2), #def 1
#                               param_name = "max_features", param_range = [1, 2, 3, 4, 5], #def 5
                              scoring = "f1_macro", cv=skf, ax=ax, n_jobs=-1)
# visualizer.show()

# dTree = DecisionTreeClassifier(random_state=0)
# dTree.fit(X_train, y_train)
# 
# accuracy = dTree.score(X_train, y_train)
# print (f"Accuracy in training: {round(accuracy,3)}")
# accuracy = dTree.score(X_test, y_test)
# print (f"Accuracy in testing: {round(accuracy,3)}")
# 
# y_predicted = dTree.predict(X_test)
# f1score = f1_score(y_test, y_predicted, average="macro")
# print(f"F1 score: {round(f1score, 3)}")
# 
# cm = confusion_matrix(y_test, y_predicted)
# print(cm)
# 
# f1LooseScore = f1_score_loose(cm)
# print(f"F1 loose score: {round(f1LooseScore, 3)}")
# 
# # K-fold validation
# skf = StratifiedKFold(n_splits=5)
# scores = cross_val_score(dTree, X, y, cv=skf, scoring="f1_macro")
# print(f"Cross validation F1 score w/ StratifiedKFold: {round(np.mean(scores),3)}")
# 
# sskf = StratifiedShuffleSplit(n_splits=10, test_size=0.2)
# scores = cross_val_score(dTree, X, y, cv=sskf, scoring="f1_macro")
# print(f"Cross validation F1 score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")
# 
# scores = cross_val_score(dTree, X, y, cv=skf, scoring=f1_loose_scorer)
# print(f"Cross validation F1 loose score w/ StratifiedKFold: {round(np.mean(scores),3)}")
# 
# scores = cross_val_score(dTree, X, y, cv=sskf, scoring=f1_loose_scorer)
# print(f"Cross validation F1 loose score w/ StratifiedShuffleSplit: {round(np.mean(scores),3)}")
# 
# 
# print(dTree.feature_importances_)
# pImportance = permutation_importance(dTree, X, y, n_repeats=100, random_state=0)
# print(pImportance["importances_mean"])


# plot_tree(dTree,
#           feature_names = featureNames,
#           class_names = ["0", "1", "2", "3"],
#           fontsize=10,
#           filled=True)
# plt.show()


# # viz_model = dtreeviz.model(clf,
# #                X_train=X_train,
# #                y_train=y_train,
# #                target_name='Class',
# #                feature_names=iris.feature_names,
# #                class_names=iris.target_names)
# # viz_model.view(scale=0.8)
