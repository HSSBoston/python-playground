import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage
import random

key = "C"
scale = [60, 62, 64, 65, 67, 69, 71]
chords = {
    "I":  [60, 64, 67], # C
    "IV": [65, 69, 72], # F
    "V":  [67, 71, 74], # G
    "VI": [69, 72, 76]  # Am
}
progression = ["I", "V", "VI", "IV"]

# MIDI setup
mid = MidiFile()
ch_track = MidiTrack()
mel_track = MidiTrack()
mid.tracks.append(ch_track)
mid.tracks.append(mel_track)

ch_track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
mel_track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))

# Generating chord progression
time_per_chord = 480
for chord in progression:
    notes = chords[chord]
    for note in notes:    
        ch_track.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(notes):
        if i==0:
            ch_track.append(Message('note_off', note=note, velocity=60, time=time_per_chord))
        else:
            ch_track.append(Message('note_off', note=note, velocity=60, time=0))

# Generating melody
for chord in progression:
    # 4 eighth notes per chord
    for _ in range(4): 
        note = random.choice(scale)
        mel_track.append(Message('note_on', note=note, velocity=80, time=0))
        mel_track.append(Message('note_off', note=note, velocity=80, time=120))

mid.save("auto_song.mid")
print("Generated a MIDI file: auto_song.mid")

# mid = MidiFile('auto_song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
