import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage
from music21 import *
from pprint import pprint

KEY_CHOICE = "a"
PROGRESSION = ["I", "IV", "V", "I"]
# progression = ["I", "V", "VI", "IV"]

OUTPUT_FILE = "random-piece4.mid"

k = key.Key(KEY_CHOICE)
print("Key choice:", k.tonic, k.mode)
print(f"Scale (Name):\t {[k.pitchFromDegree(i).nameWithOctave for i in range(1,8)]}" )
scale = [k.pitchFromDegree(i).midi for i in range(1,8)]
print(f"Scale (MIDI)\t {scale}" )

if KEY_CHOICE in ["C","D","E","F","G","A","B"]:
    rc1 = roman.RomanNumeral("I", KEY_CHOICE)
    rc2 = roman.RomanNumeral("ii", KEY_CHOICE)
    rc4 = roman.RomanNumeral("IV", KEY_CHOICE)
    rc5 = roman.RomanNumeral("V", KEY_CHOICE)
    rc6 = roman.RomanNumeral("vi", KEY_CHOICE)
    rc7 = roman.RomanNumeral("viio", KEY_CHOICE)

if KEY_CHOICE in ["c","d","e","f","g","a","b"]:
    rc1 = roman.RomanNumeral("i", KEY_CHOICE)
    rc2 = roman.RomanNumeral("iio", KEY_CHOICE)
    rc4 = roman.RomanNumeral("iv", KEY_CHOICE)
    rc5 = roman.RomanNumeral("v", KEY_CHOICE)
    rc6 = roman.RomanNumeral("VI", KEY_CHOICE)
    rc7 = roman.RomanNumeral("VII", KEY_CHOICE)

romanToChordName = {
    "I":  [p.nameWithOctave for p in rc1.pitches],
    "II": [p.nameWithOctave for p in rc2.pitches],
    "IV": [p.nameWithOctave for p in rc4.pitches],
    "V":  [p.nameWithOctave for p in rc5.pitches],
    "VI": [p.nameWithOctave for p in rc6.pitches],
    "VII":[p.nameWithOctave for p in rc7.pitches],    
    }
pprint(romanToChordName)

romanToChordMidi = {
    "I":  [p.midi for p in rc1.pitches],
    "II": [p.midi for p in rc2.pitches],
    "IV": [p.midi for p in rc4.pitches],
    "V":  [p.midi for p in rc5.pitches],
    "VI": [p.midi for p in rc6.pitches],
    "VII":[p.midi for p in rc7.pitches],
    }
pprint(romanToChordMidi)

# # MIDI setup
# midi = MidiFile()
# chordTrack = MidiTrack()
# melodyTrack = MidiTrack()
# midi.tracks.append(chordTrack)
# midi.tracks.append(melodyTrack)
# 
# TPB = 480 # ticks per beat (ticks per quater note)
# note4 = TPB
# note8 = int(TPB/2)
# note16 = int(TPB/4)
# 
# chordTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
# melodyTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(100)))
# 
# # Chord progression
# for chord in progression:
#     notes = chords[chord]
#     for note in notes:    
#         chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
#     for i, note in enumerate(notes):
#         if i==0:
#             chordTrack.append(Message('note_off', note=note, velocity=60, time=note4))
#         else:
#             chordTrack.append(Message('note_off', note=note, velocity=60, time=0))
# 
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
# midi.save(OUTPUT_FILE)
# print("Generated a MIDI file:", OUTPUT_FILE)

# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
