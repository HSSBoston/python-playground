import matplotlib.pyplot as plt
import numpy as np

N = 8
xMin = -1
xMax = 6

magnitude = np.linspace(xMin, xMax, N)
luminosity = 51 * 100**(-magnitude/5)
plt.plot(magnitude, luminosity)


for x, y in zip(magnitude, luminosity):
    plt.text(x, y, round(y, 2), ha="center", va="bottom")

plt.xlabel("Apparent Magnitude")
plt.ylabel("Luminosity")
plt.grid(True)
plt.show()
