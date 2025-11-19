from music21 import *

cMinor = chord.Chord(["C4","G4","E-5"])

print(cMinor.duration.type, cMinor.pitches)
print(cMinor.isMajorTriad(), cMinor.isMinorTriad(), cMinor.inversion())

cMajor = chord.Chord(["E3","C4","G4"])
print(cMajor.fullName)
print(cMajor.pitchedCommonName, cMajor.inversion())

print( cMajor.root(), cMajor.root().midi )
print( cMajor.bass() )
print( cMajor.third )
print( cMajor.fifth )
print( cMajor.seventh )





