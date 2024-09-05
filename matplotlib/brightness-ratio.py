import matplotlib.pyplot as plt
import numpy as np

mm1 = (100**(1/5))**5
m0 = (100**(1/5))**4
m1 = (100**(1/5))**3
m2 = (100**(1/5))**2
m3 = 100**(1/5)
m4 = 1

magnitude = np.array([-1, 0, 1, 2, 3, 4])
luminosity = np.array([mm1, m0, m1, m2, m3, m4])
plt.bar(magnitude, luminosity)

for x, y in zip(magnitude, luminosity):
    plt.text(x, y, round(y, 2), ha="center", va="bottom")

plt.xlabel("Apparent Magnitude")
plt.ylabel("Luminosity Ratio")
plt.grid(True)
plt.show()

