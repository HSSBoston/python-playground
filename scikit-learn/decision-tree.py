from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn import tree
import numpy as np

iris = load_iris()
print(type(iris))
X = iris.data   # numpy.ndarray, features
y = iris.target # numpy.ndarray, species
print (X[0:5,:])
    # Sepal Length, Sepal Width, Petal Length, Petal Width
print(y)
    # 0: Setosa
    # 1: Versicolor
    # 2: Virginica

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # 30% for testing, 70% for training
    # Deterministic (non-random) sampling

clf = tree.DecisionTreeClassifier(max_depth=3)
    # Too shallow tree: poorer classification
    # Too deep: overfitting
clf.fit(X_train, y_train)
print (clf.score(X_test, y_test))

print(y_test)
print(clf.predict(X_test))

# K分割交差検証
stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
print(f"Cross-Validation scores: {scores}")   # 各分割におけるスコア
print(f"Average score: {np.mean(scores)}")  # スコアの平均値

