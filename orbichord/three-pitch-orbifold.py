from music21.scale import ChromaticScale
from orbichord.chordinate import standardSimplex
from orbichord.generator import Generator

import holoviews as hv

hv.extension("plotly")

scale = ChromaticScale("C")

chord_generator = Generator( pitches = scale.getPitches('C','B'),
                             dimension = 3,
                             select = None )

points = []
for chord in chord_generator.run():
    points.append(standardSimplex(chord, scale))

print("Number of points:", len(points))
print("First 5 points:", points[:5])

# Plot the T^3/S_3 orbifold
plot = hv.Scatter3D(points).opts(
    padding=0.05,
    width=800,
    height=600,
    size=5 )

fig = hv.render(plot, backend="plotly")
fig.show(renderer="browser")

# fig.write_html("trichord_orbifold.html")
