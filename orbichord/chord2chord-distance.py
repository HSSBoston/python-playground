from music21.chord import Chord
from music21.scale import MajorScale
from numpy.linalg import norm
from orbichord.chordinate import EfficientVoiceLeading

vl = EfficientVoiceLeading(
    scale=MajorScale('C'),
    metric=lambda delta: norm(delta, 1)
)

movement, distance = vl(
    Chord('C E G'),
    Chord('G B D')
)

print("Movement:", movement)
print("Distance:", distance)
