from music21 import *

keyChoices = ["C", "c", "a"]

for kc in keyChoices:    
    k = key.Key(kc)
    print(k.tonic, k.mode)
    print( [k.pitchFromDegree(i).nameWithOctave for i in range(1,7)] )
    print( [k.pitchFromDegree(i).midi for i in range(1,7)] )    

cm = key.Key("a")
print(cm.mode, cm.tonic)
for i in range(1, 7):
    print( cm.pitchFromDegree(i) )
             