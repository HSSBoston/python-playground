from synthesizer import synthesizeTriad
from notes import *

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
midiData1 = [[1, initOnset,
              noteToNumber("G", 3), 100, hNote],
             [1, initOnset+qNote+qNote,
              noteToNumber("C", 3), 100, hNote],
             [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
              noteToNumber("C", 2), 100, hNote],
             [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4), 100, hNote]]
midiData2 = [[2, initOnset,
                      noteToNumber("G", 3)+2, 100, hNote],
                   [2, initOnset+qNote+qNote,
                      noteToNumber("C", 3)+2, 100, hNote],
                   [2, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2)+2, 100, hNote],
                   [2, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4)+2, 100, hNote]]
midiData3 = [[3, initOnset,
                      noteToNumber("G", 3)+4, 100, hNote],
                   [3, initOnset+qNote+qNote,
                      noteToNumber("C", 3)+4, 100, hNote],
                   [3, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2)+4, 100, hNote],
                   [3, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4)+4, 100, hNote]]

synthesizeTriad(midiData1, midiData2, midiData3, "piano", "big-dipper-piano-triad.wav")

