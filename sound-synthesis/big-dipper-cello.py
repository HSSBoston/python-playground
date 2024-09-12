from synthesizer import synthesize
from notes import *

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
midiData = [[1, initOnset,
                      noteToNumber("G", 3), 100, qNote],
                 [1, initOnset+qNote,
                      noteToNumber("E", 3), 100, qNote],
                 [1, initOnset+qNote+qNote,
                      noteToNumber("C", 3), 100, eNote],
                 [1, initOnset+qNote+qNote+eNote,
                      noteToNumber("A", 2), 80, sNote],
                 [1, initOnset+qNote+qNote+eNote+sNote,
                      noteToNumber("D", 2), 100, sNote+eNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2), 100, eNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+eNote,
                      noteToNumber("E", 2), 100, eNote+qNote],
                 [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4), 100, qNote+qNote]]

synthesize(midiData, "cello", "big-dipper-cello.wav")

