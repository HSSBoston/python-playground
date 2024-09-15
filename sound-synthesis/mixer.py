import numpy as np
from mlib.wave_file import wave_read_16bit_mono
from mlib.wave_file import wave_write_16bit_stereo

def mix(trackFileNames, outputFileName):
    number_of_track = len(trackFileNames)

    fs = 44100
    length_of_s_master = int(fs * 12)
#     track = np.zeros((length_of_s_master, number_of_track))
#     s_master = np.zeros((length_of_s_master, 2))

    fs, s= wave_read_16bit_mono(trackFileNames[0])
    track = np.zeros((len(s)+1, number_of_track))
    s_master = np.zeros((len(s)+1, number_of_track))
#     track[:, 0] = s
    print("Track", len(s)+1)
    
    for i in range(0, number_of_track):
        fs, s = wave_read_16bit_mono(trackFileNames[i])
        print("Track", i, len(s))
#         track[:, i] = s
        for n in range(len(s)):
            track[n, i] += s[n]



    v = np.array([1, 1, 1, 1])
    p = np.array([0.5, 0.5, 1, 0])

    for i in range(number_of_track):
        s_master[:, 0] += track[:, i] * v[i] * np.cos(np.pi * p[i] / 2)
        s_master[:, 1] += track[:, i] * v[i] * np.sin(np.pi * p[i] / 2)        

    master_volume = 0.9
    s_master /= np.max(np.abs(s_master))
    s_master *= master_volume

    # for n in range(int(len(s) * 0.01)):
    #     s_master[n, 0] = s_master[n, 0] * n/(fs * 0.01)
    #     s_master[n, 1] = s_master[n, 1] * n/(fs  * 0.01)

    wave_write_16bit_stereo(fs, s_master, outputFileName)
    print("Saved:", outputFileName)

if __name__ == "__main__":
    trackFileNames = ["wav/big-dipper-piano.wav",
                      "wav/big-dipper-piano-triad.wav",
                      "wav/big-dipper-violin.wav",
                      "wav/big-dipper-cello.wav"]
    mix(trackFileNames, "wav/big-dipper-mixed.wav")
    
