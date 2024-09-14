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
             noteToNumber("E", 5), 100, qNote],
            [1, initOnset+qNote,
             noteToNumber("C", 5), 100, qNote],
            [1, initOnset+qNote+qNote,
             noteToNumber("A", 4), 100, eNote],
            [1, initOnset+qNote+qNote+eNote,
                noteToNumber("F", 4), 80, sNote],
            [1, initOnset+qNote+qNote+eNote+sNote,
             noteToNumber("B", 3), 100, sNote+eNote],
            [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
             noteToNumber("A", 3), 100, eNote],
            [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+eNote,
             noteToNumber("C", 4), 100, eNote+qNote],
            [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
             noteToNumber("B", 5), 100, qNote+qNote]]

synthesize(midiData, "piano", "big-dipper-piano.wav")
synthesize(midiData, "violin", "big-dipper-violin.wav")

# synthesize(midiData, "trumpet", "big-dipper-trumpet.wav")

