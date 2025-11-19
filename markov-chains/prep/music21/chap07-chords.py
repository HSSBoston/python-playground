from music21 import *

cMajor = chord.Chord(["C4","E4","G4"])
print("Full name:", cMajor.fullName)
print("Common name:", cMajor.pitchedCommonName, ", inversion:", cMajor.inversion())
print("Pitches:", cMajor.pitches)
print(cMajor.isMajorTriad(), cMajor.isMinorTriad())
print("Duration:", cMajor.duration.type)
print("Root:", cMajor.root(), "Root MIDI:", cMajor.root().midi)
print("Bass:", cMajor.bass(), "Bass MIDI:", cMajor.bass().midi)
print("Third:", cMajor.third, "Third MIDI:", cMajor.third.midi)
print("Fifth:", cMajor.fifth, "Fifth MIDI:", cMajor.fifth.midi)
print("Seventh:", cMajor.seventh)

cMajor.inversion(0)
print(cMajor)
cMajor.inversion(1)
print(cMajor)
cMajor.inversion(2)
print(cMajor)

#closedPosition
#semiClosedPosition
#scaleDegrees

rest1 = note.Rest()
rest1.quarterLength = 0.5
noteASharp = note.Note('A#5')
noteASharp.quarterLength = 1.5

stream2 = stream.Stream()
stream2.append(cMajor)
stream2.append(rest1)
stream2.append(noteASharp)
stream2.write("midi", "chord.mid")
stream2.write("musicxml", "chord.xml")
stream2.write("text", "chord.txt")
stream2.show()


