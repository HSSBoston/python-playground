from music21.chord import Chord
from music21.scale import MajorScale
from numpy.linalg import norm
from orbichord.chordinate import EfficientVoiceLeading

vl = EfficientVoiceLeading(
    scale=MajorScale("C"),
    metric=lambda delta: norm(delta, 1) )
      # L1 distance. Other choices: 

movement, distance = vl( Chord("C E G"),
                         Chord("G B D") )

# The most efficient voice leading from C major (C–E–G) to
# G major is achieved by using G major in first inversion
# (B–D–G) rather than root position (G–B–D).

print("Movement:", movement)
print("Distance:", distance)
