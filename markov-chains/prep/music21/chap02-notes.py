from music21 import note

f = note.Note("F5")
print(f, f.name, f.octave, f.nameWithOctave)
print(f.pitch, f.pitch.frequency, f.pitch.pitchClassString, f.duration)

n = note.Note(64, type="eighth")
print(n, n.name, n.octave, n.nameWithOctave, n.pitch, n.duration)





