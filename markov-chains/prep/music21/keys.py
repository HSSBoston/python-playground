from music21 import *

keyChoices = ["C", "c", "a"]

for kc in keyChoices:    
    k = key.Key(kc)
    print(k.tonic, k.mode)
    print( [k.pitchFromDegree(i).nameWithOctave for i in range(1,8)] )
    print( [k.pitchFromDegree(i).midi for i in range(1,8)] )    

am = key.Key("a")
print(am.tonic, am.mode)
print("Relative:", am.relative)
print("Parallel", am.parallel)
print( [am.pitchFromDegree(i).nameWithOctave for i in range(1,8)] )

am3 = am.transpose(-12)
print( [am3.pitchFromDegree(i).transpose(-12).nameWithOctave for i in range(1,8)] )
             