import numpy as np

P = np.array(
    [[0.20, 0.40, 0.40],
     [0.33, 0.17, 0.50],
     [0.50, 0.33, 0.17],
     ])

state = np.zeros(3)
state[0] = 1.0
print(state)

state2 = np.dot(P.T, state)
print(P.T)
print(state2)

state2 = np.dot(state, P)
print(state2)


