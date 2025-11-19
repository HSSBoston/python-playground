from music21 import *

f = chord.Chord('F4 C5 A5')
kf = key.Key('F')
sf = stream.Measure([kf, f])
# sf.show()

kc = key.Key('C')
sc = stream.Part([kc, f])
# sc.show()

rf = roman.romanNumeralFromChord(f, kf)
print(rf)

rc = roman.romanNumeralFromChord(f, kc)
print(rc)

