from music21 import *

keyChoice = "C"

roman.RomanNumeral("I", keyChoice)



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
print(rc.figure, rc.figureAndKey, rc.romanNumeralAlone, rc.key, rc.scaleDegree)
print(rc.functionalityScore)

rc2 = roman.RomanNumeral("I", kc)
print(rc2)

rc3 = rc2 = roman.RomanNumeral("I", "C")
print(rc3)



