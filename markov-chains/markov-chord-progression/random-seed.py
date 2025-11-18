import random
import numpy as np

print(random.random(), random.random(), random.random(),
      random.random(), random.random()) 

random.seed(100);  print(random.random())
random.seed(100);  print(random.random())
# if seed=None, random() uses different seeds every time it is called.
random.seed(None); print(random.random()) 

print(random.random(), random.random(), random.random()) 

print("Numpy")
rng = np.random.default_rng()
print(rng.random(), rng.random(), rng.random())

# np.random
# 
# 
# np.random.default_rng()
