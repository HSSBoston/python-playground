from pathlib import Path

from music21.scale import ChromaticScale, MajorScale
from music21.chord import Chord
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator

import plotly.graph_objects as go

scale = MajorScale("C")

chord_generator = Generator(
    pitches=scale.getPitches("C4", "B4"),
    dimension=3,
    select=lambda chord: chord.isTriad()
)

points = [
    standardSimplex(chord, scale)
    for chord in chord_generator.run()
]

print("Number of points:", len(points))

fig = go.Figure()

# 1. Define the six vertices of the triangular prism.
# Coordinates are (x, y, z).

vertices = [
    (0, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 0),
    (1, 0, 1)
]

# 2. Add transparent prism surfaces.
# Each face of the prism is divided into triangles.

faces = [
    (0, 1, 2), (3, 4, 5),
    (0, 1, 4), (0, 4, 3),
    (0, 2, 5), (0, 5, 3),
    (1, 2, 5), (1, 5, 4)
]

i, j, k = zip(*faces)

fig.add_trace(go.Mesh3d(
    x=[v[0] for v in vertices],
    y=[v[1] for v in vertices],
    z=[v[2] for v in vertices],
    i=i, j=j, k=k,
    color="lightsteelblue",
    opacity=0.10,
    hoverinfo="skip",
    showlegend=False
))

# 3. Plot all the chords as blue points.

fig.add_trace(go.Scatter3d(
    x=[p[0] for p in points],
    y=[p[1] for p in points],
    z=[p[2] for p in points],
    mode="markers",
    marker=dict(size=3, color="royalblue", opacity=0.7),
    name="Chords"
))

# 4. Draw the nine edges of the prism.

edges = [
    (0, 1), (1, 2), (2, 0),  # First triangular end
    (3, 4), (4, 5), (5, 3),  # Second triangular end
    (0, 3), (1, 4), (2, 5)   # Three longitudinal edges
]

edge_x = []
edge_y = []
edge_z = []

for a, b in edges:
    edge_x.extend([vertices[a][0], vertices[b][0], None])
    edge_y.extend([vertices[a][1], vertices[b][1], None])
    edge_z.extend([vertices[a][2], vertices[b][2], None])

fig.add_trace(go.Scatter3d(
    x=edge_x,
    y=edge_y,
    z=edge_z,
    mode="lines",
    line=dict(color="black", width=5),
    hoverinfo="skip",
    name="Prism edges"
))

# 5. Draw the augmented-triad center line.

fig.add_trace(go.Scatter3d(
    x=[0, 1],
    y=[1/3, 1/3],
    z=[1/3, 1/3],
    mode="lines",
    line=dict(color="orange", width=6, dash="dash"),
    name="Augmented triads"
))

# 7. Improve the 3D camera and axis display.

fig.update_layout(
    title="Three-Pitch Chord Orbifold",
    width=1050,
    height=800,
    scene=dict(
        xaxis=dict(title="x (transposition)", range=[0, 1]),
        yaxis=dict(title="y (first pitch gap)", range=[0, 1]),
        zaxis=dict(title="z (second pitch gap)", range=[0, 1]),
        aspectmode="manual",
        aspectratio=dict(x=1.6, y=1, z=1),
        camera=dict(eye=dict(x=1.8, y=1.5, z=1.2))
    )
)

Path("./output").mkdir(exist_ok=True)

fig.write_html("./output/trichord_orbifold.html")
fig.show(renderer="browser")
