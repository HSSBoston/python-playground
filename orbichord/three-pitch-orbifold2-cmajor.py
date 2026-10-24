from pathlib import Path
from music21.scale import MajorScale, ChromaticScale
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator
import plotly.graph_objects as go

scale = MajorScale("C")
orbifoldScale = ChromaticScale("C")

chordGen = Generator(
    pitches=scale.getPitches("C4", "B4"),
    dimension=3,
    select=lambda chord: chord.isTriad()
)

romanMap = {
    frozenset(["C", "E", "G"]): "I (CEG)",
    frozenset(["D", "F", "A"]): "ii (DFA)",
    frozenset(["E", "G", "B"]): "iii (EGB)",
    frozenset(["F", "A", "C"]): "IV (FAC)",
    frozenset(["G", "B", "D"]): "V (GBD)",
    frozenset(["A", "C", "E"]): "vi (ACE)",
    frozenset(["B", "D", "F"]): "vii° (BDF)"
}

chordData = []

for chord in chordGen.run():
    coords = standardSimplex(chord, orbifoldScale)
    label = romanMap[frozenset(chord.pitchNames)]
    quality = chord.commonName

    chordData.append((chord, coords, label, quality))

print("Number of points:", len(chordData))

for chord, coords, label, quality in chordData:
    x, y, z = coords
    print(f"{label:20s} {quality:20s} "
          f"x={x:.4f}, y={y:.4f}, z={z:.4f}")

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
# 3. Plot diatonic triads with colors by chord quality.

colors = {
    "major triad": "royalblue",
    "minor triad": "seagreen",
    "diminished triad": "darkorange"
}

for quality, color in colors.items():

    # Select only chords of the current quality
    group = [
        (chord, coords, label)
        for chord, coords, label, q in chordData
        if q == quality
    ]

    if not group:
        continue

    fig.add_trace(go.Scatter3d(
        x=[coords[0] for chord, coords, label in group],
        y=[coords[1] for chord, coords, label in group],
        z=[coords[2] for chord, coords, label in group],

        mode="markers+text",

        marker=dict(
            size=7,
            color=color,
            opacity=0.95
        ),

        text=[label for chord, coords, label in group],
        textposition="top center",

        hovertemplate=(
            "%{text}<br>"
            "x=%{x:.4f}<br>"
            "y=%{y:.4f}<br>"
            "z=%{z:.4f}"
            "<extra></extra>"
        ),

        name=quality.title()
    ))

# 4. Draw the nine edges of the prism.
edges = [
    (0, 1), (1, 2), (2, 0),
    (3, 4), (4, 5), (5, 3),
    (0, 3), (1, 4), (2, 5)
]

edgeX = []
edgeY = []
edgeZ = []

for a, b in edges:
    edgeX.extend([vertices[a][0], vertices[b][0], None])
    edgeY.extend([vertices[a][1], vertices[b][1], None])
    edgeZ.extend([vertices[a][2], vertices[b][2], None])

fig.add_trace(go.Scatter3d(
    x=edgeX,
    y=edgeY,
    z=edgeZ,
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

fig.write_html("./output/orbifold-cmajor-diatonic-trichords.html")
fig.show(renderer="browser")
