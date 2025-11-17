import sys, time, random
import numpy as np
import sympy as sym

n_iter = 10

# Set of states (chords) 
S = ["C", "F", "G"]
# Transition probability matrix
P = np.array(
    [[0.20, 0.40, 0.40],
     [0.3, 0.1, 0.6],
     [0.50, 0.3, 0.2],
     ])

state = np.zeros(len(S))
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
    state_index = random.choices([0, 1, 2], P[state_index])[0]
    state = np.dot(state, P)
    P_r[pre_state_index, state_index] += 1.0

a, b, c = sym.symbols("a, b, c")
eq1 = sym.Eq( 0.2*a + 0.3*b + 0.5*c, a )
eq2 = sym.Eq( 0.4*a + 0.1*b + 0.3*c, b )
eq3 = sym.Eq( 0.4*a + 0.6*b + 0.2*c, c )
eq4 = sym.Eq( a+b+c, 1 )
solution = sym.solve([eq1, eq2, eq3, eq4], [a, b, c])
print(solution)




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

