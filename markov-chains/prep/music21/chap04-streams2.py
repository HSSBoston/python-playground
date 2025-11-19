from music21 import *

note1 = note.Note("C4")
note2 = note.Note("F#4")
note3 = note.Note("B-2")

stream1 = stream.Stream()
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

biggerStream = stream.Stream()
biggerStream.insert(0, note2)
biggerStream.append(stream1)

biggerStream.show("text")



