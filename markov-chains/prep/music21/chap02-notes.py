from music21 import note

f = note.Note("F5")
print(f, f.name, f.octave, f.nameWithOctave)
print(f.pitch, f.pitch.frequency, f.pitch.pitchClassString, f.pitch.midi, f.duration)

# f.show()

a = f.transpose("M3")
print(a, f.name, a.octave, a.nameWithOctave)
print(a.pitch, a.pitch.frequency, a.pitch.pitchClassString, a.duration)


n = note.Note(64, type="eighth")
print(n, n.name, n.octave, n.nameWithOctave, n.pitch, n.duration)

r = note.Rest()




