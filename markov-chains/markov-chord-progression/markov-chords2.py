import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

N = 10                 # Number of iterations (generated chords)
RANDOM_NUM_SEED = None # Non-negative int or None

# State space: set of possible states (chords) 
S = ["C", "F", "G"]
# Transition probability matrix
P = np.array(
    [[0.2, 0.4, 0.4],
     [0.3, 0.1, 0.6],
     [0.5, 0.3, 0.2],
     ])

probDist = np.zeros( (N,len(S)) )
P_r = np.zeros(P.shape)

firstChordId = 0
chordProgression = [firstChordId]
probDist[0][firstChordId] = 1.0

print(f"Step      Chord\tProb distribution over {S}")
for i in range(N-1):
    currentChordId = chordProgression[i]
    print(f"{i:0=8}: {S[currentChordId]}\t{np.round(probDist[i],4)}")
    rng = np.random.default_rng(seed=RANDOM_NUM_SEED)
    nextChordId = rng.choice([0, 1, 2], p=P[currentChordId])
    chordProgression.append(nextChordId)
    probDist[i+1] = np.dot(probDist[i], P)
    P_r[currentChordId, nextChordId] += 1.0

a, b, c = sym.symbols(", ".join(S))
eq1 = sym.Eq( 0.2*a + 0.3*b + 0.5*c, a )
eq2 = sym.Eq( 0.4*a + 0.1*b + 0.3*c, b )
eq3 = sym.Eq( 0.4*a + 0.6*b + 0.2*c, c )
eq4 = sym.Eq( a+b+c, 1 )
solution = sym.solve([eq1, eq2, eq3, eq4], [a, b, c])
print("\nStationary probability distribution")
print(solution)


print("\n> Stationary dist.")
eig_val, eig_vec = np.linalg.eig(P.T)
idx = np.argmin(np.abs(np.real(eig_val) - 1))
# Get an eigenvector correspond to the eigenvalue equal to 1.
w = np.real(eig_vec[:, idx]).T 
w /= np.sum(w) # Normalize
print(f"Recurrence relation:\t{np.round(probDist[-1],2)}")
print(f"Eigen-decomposition:\t{np.round(w,2)}\n")

# Check transition matrix
for k in range(len(S)):
    P_r[k] /= P_r[k].sum()
print("P")
print(P)
print("P_r")
print(np.round(P_r, 2))

plt.plot( probDist[:, 0] )
plt.plot( probDist[:, 1] )
plt.plot( probDist[:, 2] )
plt.show()

