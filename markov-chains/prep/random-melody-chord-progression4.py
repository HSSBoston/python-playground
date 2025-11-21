import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage

outputFile = "random-piece4.mid"

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
#   Chord notes at 70% and scale notes at 30%
#   8th and 16th notes at random
for chord in progression:
    chordNotes = chords[chord]
    remainingTicks = note4
    
    while remainingTicks > 0:
        duration = random.choice([note8, note16])
        if remainingTicks - duration < 0:
            duration = remainingTicks        
        
        if random.random() < 0.7:
            note = random.choice(chordNotes)
        else:
            note = random.choice(scale)
            
        melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
        melodyTrack.append(Message('note_off', note=note, velocity=80, time=duration))
        
        remainingTicks -= duration

midi.save(outputFile)
print("Generated a MIDI file:", outputFile)

# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
