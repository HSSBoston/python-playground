import numpy as np

v = np.zeros((3,2))
print(v)
print( v.shape )

P = np.array(
    [[0.20, 0.40, 0.40],
     [0.33, 0.17, 0.50],
     [0.50, 0.33, 0.17],
     ])
     
P_cum = [np.array([P[m, 0:n+1].sum() for n in range(P.shape[1])]) for m in range(P.shape[0])]
print(P_cum)

