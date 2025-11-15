import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage

outputFile = "random-band.mid"

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
bassTrack = MidiTrack()
drumTrack = MidiTrack()
midi.tracks.append(chordTrack)
midi.tracks.append(melodyTrack)
midi.tracks.append(bassTrack)
midi.tracks.append(drumTrack)

TPB = 480 # ticks per beat (ticks per quater note)
note4 = TPB
note2 = int(note4*2)
note8 = int(TPB/2)
note16 = int(TPB/4)
note32 = int(TPB/8)

chordTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
melodyTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))

# Chord progression
for chord in progression:
    notes = chords[chord]
    for note in notes:    
        chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(notes):
        if i==0:
            chordTrack.append(Message('note_off', note=note, velocity=50, time=note4))
        else:
            chordTrack.append(Message('note_off', note=note, velocity=50, time=0))

# # Melody
# #   Chord notes at 70% and scale notes at 30%
# #   8th and 16th notes at random
# for chord in progression:
#     chordNotes = chords[chord]
#     remainingTicks = note4
#     
#     while remainingTicks > 0:
#         duration = random.choice([note8, note16])
#         if remainingTicks - duration < 0:
#             duration = remainingTicks        
#         
#         if random.random() < 0.7:
#             note = random.choice(chordNotes)
#         else:
#             note = random.choice(scale)
#             
#         melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
#         melodyTrack.append(Message('note_off', note=note, velocity=80, time=duration))
#         
#         remainingTicks -= duration
# 
# # Bass
# for chord in progression:
#     root = chords[chord][0] - 24
#     remainingTicks = note4
#     
#     while remainingTicks > 0:
#         duration = random.choice([note4, note8])
#         if remainingTicks - duration < 0:
#             duration = remainingTicks
#         
#         bassTrack.append(Message('note_on', note=root, velocity=90, time=0))
#         bassTrack.append(Message('note_off', note=root, velocity=90, time=duration))
#         remainingTicks -= duration
    
# Dram
for _ in progression:
    for step in range(0, note4, note16):
        # Kick
        if step == 0:
            drumTrack.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
            drumTrack.append(Message('note_off', note=36, velocity=100, time=note16, channel=9))
        # Snare
        if(step == note16) or (step == note16*3):
            drumTrack.append(Message('note_on', note=38, velocity=100, time=0, channel=9))
            drumTrack.append(Message('note_off', note=38, velocity=100, time=note16, channel=9))
        # Hihut
        drumTrack.append(Message('note_on', note=42, velocity=70, time=0, channel=9))
        drumTrack.append(Message('note_off', note=42, velocity=70, time=note16, channel=9))
        


midi.save(outputFile)
print("Generated a MIDI file:", outputFile)

# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
