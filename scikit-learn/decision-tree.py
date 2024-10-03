from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn import tree
import numpy as np, dtreeviz
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()
# print(type(iris))
X = iris.data   # numpy.ndarray, features
y = iris.target # numpy.ndarray, species
print (X[0:5,:])
    # Sepal Length, Sepal Width, Petal Length, Petal Width
print(y)
    # 0: Setosa
    # 1: Versicolor
    # 2: Virginica
print(f"Feature names: {iris.feature_names}")
print(f"Class names: {iris.target_names}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # 30% for testing, 70% for training
    # Deterministic (non-random) sampling

clf = tree.DecisionTreeClassifier(max_depth=3)
    # Too shallow tree: poorer classification
    # Too deep: overfitting
clf.fit(X_train, y_train)
print ("Accuracy:", clf.score(X_test, y_test))

print(f"Correct result: {y_test}")
print(f"Predicted:      {clf.predict(X_test)}")

# K分割交差検証
stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
# print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
print(f"Cross validation score: {np.mean(scores)}")  # スコアの平均値

print( clf.feature_importances_)

plot_tree(clf,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          fontsize=10,
          filled=True)
plt.show()

# viz_model = dtreeviz.model(clf,
#                X_train=X_train,
#                y_train=y_train,
#                target_name='Class',
#                feature_names=iris.feature_names,
#                class_names=iris.target_names)
# viz_model.view(scale=0.8)
