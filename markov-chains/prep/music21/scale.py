from music21 import *

sc1 = scale.MajorScale("C")
print(sc1)

sc1 = scale.MajorScale("c")
print(sc1)

ds1 = scale.DiatonicScale("C3")
print(ds1.name)
print(ds1.tonic)
print(ds1.pitches)
