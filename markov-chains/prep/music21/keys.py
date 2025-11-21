from music21 import *

c = key.Key("C")
print(c.mode, c.tonic)
for i in range(1, 7):
    print( c.pitchFromDegree(i) )

cm = key.Key("c")
print(cm.mode, cm.tonic)
for i in range(1, 7):
    print( cm.pitchFromDegree(i) )

cm = key.Key("a")
print(cm.mode, cm.tonic)
for i in range(1, 7):
    print( cm.pitchFromDegree(i) )
             