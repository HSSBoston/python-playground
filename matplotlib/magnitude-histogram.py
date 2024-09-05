import matplotlib.pyplot as plt
import numpy as np

# 1等星以上 	21
#     -1等星 2
#     0等星 7
#     1等星 12

mm1 = 2
m0 = 7
m1 = 12
m2 = 67
m3 = 190
m4 = 710
m5 = 2000
m6 = 5600

magnitude = np.array([-1, 0, 1, 2, 3, 4, 5, 6])
starCount = np.array([mm1, m0, m1, m2, m3, m4, m5, m6])
plt.bar(magnitude, starCount)

for x, y in zip(magnitude, starCount):
    plt.text(x, y, y, ha="center", va="bottom")

plt.xlabel("Apparent Magnitude")
plt.ylabel("Number of Stars")
plt.grid(True)
plt.show()

