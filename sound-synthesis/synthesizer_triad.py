import numpy as np
from notes import *
from wave_file import wave_write_16bit_mono
from musical_instruments import acoustic_piano, acoustic_guitar, pipe_organ, cello, contrabass, trombone

masterVolume = 0.9
samplingFreq = 44100
initOnset = 0.5
trackCount = 3

def synthTriad(score1, score2, score3, instrument, outputFileName):
    noteCount = score1.shape[0]

    score = np.append(score1, score2, axis=0)
    score = np.append(score, score3, axis=0)
    scoreDuration = score[ noteCount-1 ][1] + score[ noteCount-1 ][4]
    masterDuration = scoreDuration + 1

    print("Score duration: ", scoreDuration)
    print("Master duration: ", masterDuration)

    masterSamplesCount = int(samplingFreq * masterDuration)
    masterSamples = np.zeros(masterSamplesCount)
    
    for i in range(score.shape[0]):
        print("\tTrack #", int(score[i, 0]), " instrument, Note #", i%noteCount)
        onset = score[i, 1]
#         print(onset)
        noteNumber = int(score[i, 2])
#         print(noteNumber)
        velocity = score[i, 3]
#         print(velocity)
        gate = score[i, 4]
#         print(gate)
        if instrument=="piano":
            samples = acoustic_piano(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="violin":
            samples = violin(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="harp":
            samples = harp(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="acoustic_guitar":
            samples = acoustic_guitar(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="pipe_organ":
            samples = pipe_organ(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="harpsichord":
            samples = harpsichord(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="electric_piano":
            samples = electric_piano(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="cello":
            samples = cello(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="contrabass":
            samples = contrabass(samplingFreq, noteNumber, velocity, gate)
        elif instrument=="trombone":            
            samples = trombone(samplingFreq, noteNumber, velocity, gate)
    
        offset = int(samplingFreq * onset)
        for n in range(len(samples)):
            masterSamples[offset -1 + n] += samples[n]

    for n in range(int(samplingFreq * 0.01)):
        masterSamples[n] = masterSamples[n] * n/(samplingFreq * 0.01)
        
    masterSamples = masterSamples/np.max(np.abs(masterSamples))
    masterSamples = masterSamples * masterVolume
    
    outputFileName = "wav/" + outputFileName
    wave_write_16bit_mono(samplingFreq, masterSamples, outputFileName)
    print("\tSaved:", outputFileName)

if __name__ == "__main__":
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

    synthTriad(score1, score2, score3, "piano", "big-dipper-bass-cmajor-triad-piano.wav")


