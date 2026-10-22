from music21.scale import ChromaticScale
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator

import plotly.express as px

scale = ChromaticScale("C")

chord_generator = Generator( pitches = scale.getPitches('C','B'),
                             dimension = 3,
                             select = None )

points = []
for chord in chord_generator.run():
    points.append(standardSimplex(chord, scale))

print("Number of points:", len(points))
print("First 5 points:", points[:5])

fig = px.scatter(
    x=[p[1] for p in points],
    y=[p[2] for p in points],
    labels={"x": "y", "y": "z"} )

fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.show(renderer="browser")
