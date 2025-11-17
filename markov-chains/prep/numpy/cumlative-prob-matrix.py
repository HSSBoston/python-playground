import numpy as np

# v = np.zeros((3,2))
# print(v)
# print( v.shape )

P = np.array(
    [[0.20, 0.40, 0.40],
     [0.33, 0.17, 0.50],
     [0.50, 0.33, 0.17],
     ])
# print(P)

cumulativeP = np.zeros((P.shape[0], P.shape[1]))
# print(cumulativeP)

for row_i in range(P.shape[0]):
    for column_i in range(P.shape[1]):
        cumulativeP[row_i][column_i] = P[row_i, 0:column_i+1].sum()
print(cumulativeP)

P_cum = [np.array([P[m, 0:n+1].sum() for n in range(P.shape[1])]) for m in range(P.shape[0])]
print(P_cum)

