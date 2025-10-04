import matplotlib.pyplot as plt
import numpy as np

categories = ["Temp", "PFSI", "Precip", "Windspeed"]
values = [0.4, 0.3, 0.5, 0.2]

num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
angles += angles[:1]
values += values[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, values, linewidth=1, linestyle="solid", label="Tasmania")
ax.fill(angles, values, "blue", alpha=0.1)

# Draw labels
ax.set_thetagrids(np.degrees(angles[:-1]), categories,
                  fontsize=16, fontweight='bold', color="purple")
ax.set_ylim(0, 1)
# ax.set_title("Rader Chart for Fishing Spots")
ax.legend()
plt.show()