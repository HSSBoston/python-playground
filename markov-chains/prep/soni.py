from music21 import *
import pprint

KEY_CHOICE = "C"
PROGRESSION = ["I", "IV", "V", "I"]

k = key.Key(KEY_CHOICE)
#print(k)

if k.mode == "major":
  sc = scale.MajorScale(KEY_CHOICE)
else:
  sc = scale.MinorScale(KEY_CHOICE)

scalePitchNames = []
scaleMidi = []

start = k.tonic
start.octave = 4

for p in sc.getPitches():
  scalePitchNames.append(p.nameWithOctave)
  scaleMidi.append(p.midi)

scalePitchNames = scalePitchNames[0:-1]
scaleMidi = scaleMidi[0:-1]
print(scalePitchNames)
print(scaleMidi)

if k.mode == "major":
    rn1 = roman.RomanNumeral("I", sc)
    rn2 = roman.RomanNumeral("ii", sc)
    rn4 = roman.RomanNumeral("IV", sc)
    rn5 = roman.RomanNumeral("V", sc)
    rn6 = roman.RomanNumeral("vi", sc)
    rn7 = roman.RomanNumeral("viio", sc)
else:
    rn1 = roman.RomanNumeral("i", sc)
    rn2 = roman.RomanNumeral("iio", sc)
    rn4 = roman.RomanNumeral("iv", sc)
    rn5 = roman.RomanNumeral("v", sc)
    rn6 = roman.RomanNumeral("VI", sc)
    rn7 = roman.RomanNumeral("VII", sc)
"""
romanToChordTones = {}
romanToChordTonesMidi = {}

chordTones=[]
for p in rn1.pitches:
  chordTones.append(p.nameWithOctave)
romanToChordTones["I"] = chordTones
"""
romanToChordTones = {
    "I":  [p.nameWithOctave for p in rn1.pitches],
    "II": [p.nameWithOctave for p in rn2.pitches],
    "IV": [p.nameWithOctave for p in rn4.pitches],
    "V":  [p.nameWithOctave for p in rn5.pitches],
    "VI": [p.nameWithOctave for p in rn6.pitches],
    "VII":[p.nameWithOctave for p in rn7.pitches],
    }
romanToChordTonesMidi = {
    "I":  [p.midi for p in rn1.pitches],
    "II": [p.midi for p in rn2.pitches],
    "IV": [p.midi for p in rn4.pitches],
    "V":  [p.midi for p in rn5.pitches],
    "VI": [p.midi for p in rn6.pitches],
    "VII":[p.midi for p in rn7.pitches],
    }

pprint.pprint(romanToChordTones)
pprint.pprint(romanToChordTonesMidi)

melody = stream.Part()
m1Chord = stream.Measure()

m1Melody = stream.Measure()
m1Chord.timeSignature = meter.TimeSignature()
m1Melody.timeSignature = meter.TimeSignature()
m1Chord.keySignature = key.Key(KEY_CHOICE)
m1Melody.keySignature = key.Key(KEY_CHOICE)
m2Chord = stream.Measure()
m2Melody = stream.Measure()
m2Chord.rightBarLine = bar.Barline("final")
m2Melody.rightBarLine = bar.Barline("final")

chords = stream.Part()

count = 0
for num in PROGRESSION:
  count += 1 
  print(romanToChordTones[num])
  print(romanToChordTonesMidi[num])
  c = chord.Chord(romanToChordTones[num])
  c.quarterLength = 2
  if count <= 2:
    m1Chord.append(c)
  else:
    m2Chord.append(c)
  
chords.append([m1Chord,m2Chord])
melody.append(note.Note("G"))
s = stream.Score([melody,chords])
s.show()
