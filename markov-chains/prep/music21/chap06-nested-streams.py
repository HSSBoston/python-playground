from music21 import *
from pprint import pprint

sBach = corpus.parse('bach/bwv57.8')

print( len(sBach) )
pprint( [e for e in sBach] )
# print( len(sBach[3]) )
# print( len(sBach[3][1]) )

# print( len(sBach.getElementsByClass(stream.Part)) )
# print( len(sBach.getElementsByClass("Part")) )
print( len(sBach.parts) )

for p in sBach.parts:
    print(p.partName, len(p), p.duration)

excerpt = sBach.parts[0].measures(1,4)
excerpt.show()

sBach.show("text")


