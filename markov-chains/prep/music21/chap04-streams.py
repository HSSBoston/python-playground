from music21 import *

note1 = note.Note("C4")
note2 = note.Note("F#4")
note3 = note.Note("B-2")

stream1 = stream.Stream()
stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

stream1.show("text")
# stream1.show()

print(stream1)
print( stream1[0], stream1[-1], stream1[-2] )
print( stream1[0:3] )

stream1.pop( stream1.index(note2) )
stream1.append(note2)
# stream1.show()

for n in stream1:
    print(n.offset, n.name)

# stream1.show("midi")

print( stream1.duration )

