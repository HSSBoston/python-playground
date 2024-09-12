# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
wNote, hNote, eNote, sNote, tNote = (qNote*4, qNote*2, qNote/2, qNote/4, qNote/8)

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
score1 = np.array([[1, initOnset,
                      noteToNumber("G", 3), 100, hNote],
                   [1, initOnset+qNote+qNote,
                      noteToNumber("C", 3), 100, hNote],
                   [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2), 100, hNote],
                   [1, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4), 100, hNote]] )
score2 = np.array([[2, initOnset,
                      noteToNumber("G", 3)+2, 100, wNote],
                   [2, initOnset+qNote+qNote,
                      noteToNumber("C", 3)+2, 100, hNote],
                   [2, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2)+2, 100, hNote],
                   [2, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4)+2, 100, hNote]] )
score3 = np.array([[3, initOnset,
                      noteToNumber("G", 3)+4, 100, hNote],
                   [3, initOnset+qNote+qNote,
                      noteToNumber("C", 3)+4, 100, hNote],
                   [3, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote,
                      noteToNumber("C", 2)+4, 100, hNote],
                   [3, initOnset+qNote+qNote+eNote+sNote+sNote+eNote+eNote+sNote+eNote+qNote,
                      noteToNumber("D", 4)+4, 100, hNote]] )

synth("piano")

