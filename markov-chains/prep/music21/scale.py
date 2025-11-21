from music21 import *

sc = scale.MajorScale("C")
print(sc.name)
print(sc.tonic)
print([p.nameWithOctave for p in sc.pitches])

sc = scale.MajorScale("C4")
print(sc.name)
print(sc.tonic)
print([p.nameWithOctave for p in sc.pitches])

k = key.Key("a")
sc = scale.DiatonicScale(k.tonic)
print(sc.name)
print(sc.tonic)
print([p.nameWithOctave for p in sc.pitches])


sc1 = scale.MajorScale("c")
print(sc1)

ds1 = scale.DiatonicScale("c4")
