import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage

outputFile = "random-piece.mid"

key = "C" # C major
scale = [60, 62, 64, 65, 67, 69, 71]
chords = {
    "I":  [60, 64, 67], # C
    "IV": [65, 69, 72], # F
    "V":  [67, 71, 74], # G
    "VI": [69, 72, 76]  # Am
}
progression = ["I", "IV", "V", "I"]
# progression = ["I", "V", "VI", "IV"]

# MIDI setup
midi = MidiFile()
chordTrack = MidiTrack()
melodyTrack = MidiTrack()
midi.tracks.append(chordTrack)
midi.tracks.append(melodyTrack)

TPB = 480 # ticks per beat (ticks per quater note)
note4 = TPB
note8 = int(TPB/2)
note16 = int(TPB/4)

chordTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
melodyTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))

# Chord progression
for chord in progression:
    notes = chords[chord]
    for note in notes:    
        chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(notes):
        if i==0:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=note4))
        else:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=0))

# Melody
for chord in progression:
    # 16 eighth notes per chord
    for _ in range(4): 
        note = random.choice(scale)
        melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
        melodyTrack.append(Message('note_off', note=note, velocity=80, time=note16))

midi.save(outputFile)
print("Generated a MIDI file:", outputFile)

# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
