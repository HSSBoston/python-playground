import sys
import time
import numpy as np
import matplotlib.pyplot as plt


S = ["C", "F", "G"]
P = np.array(
    [[0.20, 0.40, 0.40],
     [0.33, 0.17, 0.50],
     [0.50, 0.33, 0.17],
     ])

     
n_iter = int(sys.argv[1])
state = np.zeros(len(S))
P_cum = [np.array([P[m, 0:n+1].sum() for n in range(P.shape[1])]) for m in 
range(P.shape[0])]
P_r = np.zeros(P.shape)
state_index = 0
state[state_index] = 1.0
print(f"Step      State\tStationary")
print(f"=====================================")
for iter in range(0, n_iter):
    print(f"{iter:0=8}: {S[state_index]}\t{np.round(state,4)}")
    # Transition
    r = np.random.random()
    pre_state_index = state_index
    state_index = np.where(P_cum[state_index] > r)[0][0]
    state = np.dot(P.T, state)
    P_r[pre_state_index, state_index] += 1.0
    time.sleep(0.0001)

print("\n> Stationary dist.")
eig_val, eig_vec = np.linalg.eig(P.T)
idx = np.argmin(np.abs(np.real(eig_val) - 1))
# Get an eigenvector correspond to the eigenvalue equal to 1.
w = np.real(eig_vec[:, idx]).T 
w /= np.sum(w) # Normalize
print(f"Recurrence relation:\t{np.round(state,2)}")
print(f"Eigen-decomposition:\t{np.round(w,2)}\n")

# Check transition matrix
for k in range(len(S)):
    P_r[k] /= P_r[k].sum()
print("P")
print(P)
print("P_r")
print(np.round(P_r, 2))

