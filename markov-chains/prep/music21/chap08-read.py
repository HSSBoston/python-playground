from music21 import *
from pprint import pprint

s = converter.parse("./chord.musicxml")

print( len(s) )
pprint( [e for e in s] )
# print( len(sBach[3]) )
# print( len(sBach[3][1]) )

# print( len(sBach.getElementsByClass(stream.Part)) )
# print( len(sBach.getElementsByClass("Part")) )

print( len(s.parts) )

for p in s.parts:
    print(p.partName, len(p), p.duration)

# excerpt = sBach.parts[0].measures(1,4)
# excerpt.show()
# 
# sBach.show("text")
