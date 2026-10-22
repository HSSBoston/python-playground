from music21.scale import ChromaticScale
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator
from music21.chord import Chord

import plotly.express as px

scale = ChromaticScale("C")
chord_generator = Generator( pitches = scale.getPitches('C','B'),
                             dimension = 3,
                             select = None )
points = []
for chord in chord_generator.run():
    points.append(standardSimplex(chord, scale))
print("Number of points:", len(points))

# Count distinct points in the yz projection
uniqueYzPoints = { (round(p[1], 8), round(p[2], 8)) for p in points }
print("Distinct 2D points:", len(uniqueYzPoints))

fig = px.scatter(
    x=[p[1] for p in points],
    y=[p[2] for p in points],
    labels={"x": "y", "y": "z"} )

chords = {
    "C major":      Chord("C4 E4 G4"),
    "C minor":      Chord("C4 E-4 G4"),
    "C aug":  Chord("C4 E4 G#4"),
    "C dim": Chord("C4 E-4 G-4") }

for name, chord in chords.items():
    x, y, z = standardSimplex(chord, scale)
    print(name)
    print("  y =", round(y, 4))
    print("  z =", round(z, 4))
    print("  Remaining gap =", round(1 - y - z, 4))

    fig.add_scatter(
        x=[y],
        y=[z],
        mode="markers+text",
        text=[name],
        textposition="top center",
        marker=dict(color="red", size=12),
        name=name )

fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show(renderer="browser")
