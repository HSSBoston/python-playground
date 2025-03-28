from synthesizer import synthesizeTracks
from notes import *

initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
midiData1 = [[1, initOnset, noteToNumber("G", 3), 100, 20]]
midiData2 = [[2, initOnset, noteToNumber("D", 4), 100, 20]]
midiData3 = [[3, initOnset, noteToNumber("A", 4), 100, 20]]
midiData4 = [[4, initOnset, noteToNumber("E", 5), 100, 20]]

synthesizeTracks([midiData1, midiData2, midiData3, midiData4], "violin", "violin4.wav")

