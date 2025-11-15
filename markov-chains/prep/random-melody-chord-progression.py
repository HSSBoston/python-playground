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
# ticks_per_beat=480
midi = MidiFile()
chordTrack = MidiTrack()
melodyTrack = MidiTrack()
midi.tracks.append(chordTrack)
midi.tracks.append(melodyTrack)

chordTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
melodyTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))

# Chord progression
time_per_chord = 480
for chord in progression:
    notes = chords[chord]
    for note in notes:    
        chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(notes):
        if i==0:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=time_per_chord))
        else:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=0))

# Melody
for chord in progression:
    # 4 eighth notes per chord
    for _ in range(4): 
        note = random.choice(scale)
        melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
        melodyTrack.append(Message('note_off', note=note, velocity=80, time=120))

midi.save("auto_song.mid")
print("Generated a MIDI file: auto_song.mid")

# midi = MidiFile('auto_song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
