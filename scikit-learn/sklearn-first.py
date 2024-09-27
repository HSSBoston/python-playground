from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree


iris = load_iris()
X = iris.data   # numpy.ndarray
y = iris.target # numpy.ndarray

print(type(X))
print(type(y))

print (X[0:5,:])
    # Sepal Length, Sepal Width, Petal Length, Petal Width
print(y)
    # 0: Setosa
    # 1: Versicolor
    # 2: Virginica
