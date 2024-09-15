import numpy as np
from notes import *
from mlib.wave_file import wave_write_16bit_mono, wave_read_16bit_mono
from mlib.musical_instruments import acoustic_piano, violin, cello, trumpet
from sound_effects import reverb

masterVolume = 0.9
samplingFreq = 44100

def synthesize(midiData, instrument, outputFileName):
    score = np.array(midiData)
    noteCount = score.shape[0]
    synth(score, noteCount, instrument, outputFileName)

def synthesizeTriad(midiData1, midiData2, midiData3, instrument, outputFileName):
    score = np.append(midiData1, midiData2, axis=0)
    score = np.append(score, midiData3, axis=0)
    noteCount = len(midiData1)
    synth(score, noteCount, instrument, outputFileName)

def synth(score, noteCount, instrument, outputFileName):
    scoreDuration = score[ noteCount-1 ][1] + score[ noteCount-1 ][4]
    masterDuration = scoreDuration + 1
    print("Score duration:", scoreDuration)
    print("Master duration:", masterDuration)

    masterSamplesCount = int(samplingFreq * masterDuration)
    masterSamples = np.zeros(masterSamplesCount)
    
    initOnSet = score[0, 1]

    for i in range(score.shape[0]):
            print("\tTrack #", int(score[i, 0]), instrument, "Note #", i%noteCount)
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
            elif instrument=="trumpet":
                samples = trumpet(samplingFreq, noteNumber, velocity, gate)
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
    
    # Fade-in effect
#     for n in range(int(samplingFreq * initOnSet)-1,
#                    int(samplingFreq * (initOnSet + 0.01) )):
#         masterSamples[n] = masterSamples[n] * n/(samplingFreq * 0.01)
        
#     masterSamples = masterSamples/np.max(np.abs(masterSamples))
#     masterSamples = masterSamples * masterVolume
##    masterSamples = masterSamples * velocity/127
    
    outputFileName = "wav/" + outputFileName
    wave_write_16bit_mono(samplingFreq, masterSamples, outputFileName)
    print("\tSaved:", outputFileName)
    
    _, samples = wave_read_16bit_mono(outputFileName)
    reverbTime = 1
    reverbLevel = 0.1
    samples = reverb(samplingFreq, reverbTime, reverbLevel, samples)
    wave_write_16bit_mono(samplingFreq, samples.copy(),
                          outputFileName.split(".")[0] + "-reverb.wav")
    print("\tSaved:", outputFileName)

if __name__ == "__main__":
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
#     synthesize(midiData, "violin", "big-dipper-violin.wav")

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

#     synthTriad(midiData1, midiData2, midiData3, "piano", "big-dipper-piano-triad.wav")

