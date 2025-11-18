from music21 import *

bwv295 = corpus.parse('bach/bwv295')
for thisNote in bwv295.recurse().notes:
  thisNote.addLyric(thisNote.pitch.german)
bwv295.show()
