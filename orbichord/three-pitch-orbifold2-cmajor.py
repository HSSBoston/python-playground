from pathlib import Path

from music21.scale import MajorScale
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator

import plotly.graph_objects as go

scale = MajorScale("C")

chord_generator = Generator(
    pitches=scale.getPitches("C4", "B4"),
    dimension=3,
    select=lambda chord: chord.isTriad()
)

# Map each diatonic triad in C major to a Roman numeral label
roman_map = {
    frozenset(["C", "E", "G"]):  "I",
    frozenset(["D", "F", "A"]):  "ii",
    frozenset(["E", "G", "B"]):  "iii",
    frozenset(["F", "A", "C"]):  "IV",
    frozenset(["G", "B", "D"]):  "V",
    frozenset(["A", "C", "E"]):  "vi",
    frozenset(["B", "D", "F"]):  "vii°"
}

# Store chord, coordinates, and label
chord_data = []
for chord in chord_generator.run():
    coords = standardSimplex(chord, scale)
    pitch_set = frozenset(chord.pitchNames)
    roman = roman_map.get(pitch_set, "?")
    pitch_label = "-".join(chord.pitchNames)
    full_label = f"{roman} ({pitch_label})"
    chord_data.append((chord, coords, roman, pitch_label, full_label))

print("Number of points:", len(chord_data))
print()

print("Generated diatonic triads in C major:")
for chord, (x, y, z), roman, pitch_label, full_label in chord_data:
    print(f"{full_label:18s}   x={x:.4f}, y={y:.4f}, z={z:.4f}")

fig = go.Figure()

# 1. Define the six vertices of the triangular prism.
vertices = [
    (0, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 0),
    (1, 0, 1)
]

# 2. Add transparent prism surfaces.
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

# 3. Plot the C-major diatonic triads as labeled blue points.
x_vals = [coords[0] for chord, coords, roman, pitch_label, full_label in chord_data]
y_vals = [coords[1] for chord, coords, roman, pitch_label, full_label in chord_data]
z_vals = [coords[2] for chord, coords, roman, pitch_label, full_label in chord_data]

plot_labels = [full_label for chord, coords, roman, pitch_label, full_label in chord_data]

hover_labels = [
    f"{full_label}<br>x={coords[0]:.4f}, y={coords[1]:.4f}, z={coords[2]:.4f}"
    for chord, coords, roman, pitch_label, full_label in chord_data
]

fig.add_trace(go.Scatter3d(
    x=x_vals,
    y=y_vals,
    z=z_vals,
    mode="markers+text",
    marker=dict(size=6, color="royalblue", opacity=0.9),
    text=plot_labels,
    textposition="top center",
    hovertext=hover_labels,
    hoverinfo="text",
    name="C-major diatonic triads"
))

# 4. Draw the nine edges of the prism.
edges = [
    (0, 1), (1, 2), (2, 0),
    (3, 4), (4, 5), (5, 3),
    (0, 3), (1, 4), (2, 5)
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
    name="Augmented-triad line"
))

# 6. Improve layout.
fig.update_layout(
    title="C-Major Diatonic Triads",
    width=1150,
    height=850,
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

fig.write_html("./output/orbifold-cmajor-diatonic-trichords.html.html")
fig.show(renderer="browser")
