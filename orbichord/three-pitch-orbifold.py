from orbichord.generator import Generator

import holoviews as hv
from holoviews import opts

hv.extension("plotly")
hv.output(size=180)

scale = ChromaticScale("C")

chord_generator = Generator( pitches = scale.getPitches('C','B'),
                             dimension = 3,
                             select = None )




