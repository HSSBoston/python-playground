import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.where(a < 4))
# (array([0, 0, 0, 1]), array([0, 1, 2, 0]))

print(type(np.where(a < 4)))
# <class 'tuple'>

print(type(np.where(a < 4)[0]))
# <class 'numpy.ndarray'>
