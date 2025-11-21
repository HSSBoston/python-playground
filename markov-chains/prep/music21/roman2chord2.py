from music21 import *
from pprint import pprint

keyChoice = "c"

if keyChoice in ["C","D","E","F","G","A","B"]:
    rc1 = roman.RomanNumeral("I", keyChoice)
    rc2 = roman.RomanNumeral("ii", keyChoice)
    rc4 = roman.RomanNumeral("IV", keyChoice)
    rc5 = roman.RomanNumeral("V", keyChoice)
    rc6 = roman.RomanNumeral("vi", keyChoice)
    rc7 = roman.RomanNumeral("viio", keyChoice)

if keyChoice in ["c","d","e","f","g","a","b"]:
    rc1 = roman.RomanNumeral("i", keyChoice)
    rc2 = roman.RomanNumeral("iio", keyChoice)
    rc4 = roman.RomanNumeral("iv", keyChoice)
    rc5 = roman.RomanNumeral("v", keyChoice)
    rc6 = roman.RomanNumeral("VI", keyChoice)
    rc7 = roman.RomanNumeral("VII", keyChoice)

romanToChordName = {
    "I":  [p.nameWithOctave for p in rc1.pitches],
    "II": [p.nameWithOctave for p in rc2.pitches],
    "IV": [p.nameWithOctave for p in rc4.pitches],
    "V":  [p.nameWithOctave for p in rc5.pitches],
    "VI": [p.nameWithOctave for p in rc6.pitches],
    "VII":[p.nameWithOctave for p in rc7.pitches],    
    }
pprint(romanToChordName)

romanToChordMidi = {
    "I":  [p.midi for p in rc1.pitches],
    "II": [p.midi for p in rc2.pitches],
    "IV": [p.midi for p in rc4.pitches],
    "V":  [p.midi for p in rc5.pitches],
    "VI": [p.midi for p in rc6.pitches],
    "VII":[p.midi for p in rc7.pitches],
    }
pprint(romanToChordMidi)

print(rc1.figure, rc1.figureAndKey, rc1.romanNumeralAlone, rc1.key, rc1.scaleDegree)
print(rc1.functionalityScore)
if rc1.figure=="I":
    print("Yes", rc1.figure)
if rc1.scaleDegree==1:
    print("Yes", rc1.scaleDegree)

chords = [rc1, rc2, rc4, rc5, rc6, rc7]
for chord in chords:
    for p in chord.pitches:
        print(chord.figure, p, p.midi)
    

