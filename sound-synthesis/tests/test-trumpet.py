import sys, os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../"))

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

# midiData = [[1, initOnset,
#             noteToNumber("A", 4), 110, hNote]]

midiData = [[1, initOnset,
            noteToNumber("A", 4), 110, hNote],
            [1, initOnset+hNote,
             noteToNumber("A", 4), 0, hNote]]

# midiData = [[1, initOnset,
#             noteToNumber("A", 4), 110, hNote],
#             [1, initOnset+hNote+tNote,
#              noteToNumber("A", 4), 0, hNote-tNote]]

# midiData = [[1, initOnset,
#              noteToNumber("C", 4), 96, hNote],
#             [1, initOnset+hNote,
#              noteToNumber("C", 4), 32, hNote]]

synthesize(midiData, "trumpet", "test-trumpet.wav")

