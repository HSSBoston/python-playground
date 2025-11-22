import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage
from music21 import *
from pprint import pprint

KEY_CHOICE = "a"
PROGRESSION = ["I", "IV", "V", "I"]
# PROGRESSION = ["I", "V", "VI", "IV"]

BPM = 100
OUTPUT_FILE = "random-piece4.mid"

k = key.Key(KEY_CHOICE)
print("Key choice:", k.tonic, k.mode)

if k.mode == "major":
    scale = k.getScale("major")
else:
    scale = k.getScale("minor")
    if scale.tonic.name in ["A", "B"]:
        scale.tonic = pitch.Pitch(scale.tonic.name, octave=3)

print(f"Scale tonic: {scale.getTonic()}\t {[p.nameWithOctave for p in scale.getPitches()[:-1]]}" )
scaleMidi = [p.midi for p in scale.getPitches()[:-1]]
print(f"Scale (MIDI)\t {scaleMidi}" )
 
if k.mode == "major":
    rc1 = roman.RomanNumeral("I", scale)
    rc2 = roman.RomanNumeral("ii", scale)
    rc4 = roman.RomanNumeral("IV", scale)
    rc5 = roman.RomanNumeral("V", scale)
    rc6 = roman.RomanNumeral("vi", scale)
    rc7 = roman.RomanNumeral("viio", scale)
else:
    rc1 = roman.RomanNumeral("i", scale)
    rc2 = roman.RomanNumeral("iio", scale)
    rc4 = roman.RomanNumeral("iv", scale)
    rc5 = roman.RomanNumeral("v", scale)
    rc6 = roman.RomanNumeral("VI", scale)
    rc7 = roman.RomanNumeral("VII", scale)

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

# MIDI setup
midi = MidiFile()
chordTrack = MidiTrack()
melodyTrack = MidiTrack()
midi.tracks.append(chordTrack)
midi.tracks.append(melodyTrack)

TPB    = 480 # ticks per beat (ticks per quater note)
NOTE1  = TPB * 4
NOTE2  = TPB * 2
NOTE4  = TPB
NOTE8  = int(TPB/2)
NOTE16 = int(TPB/4)

chordTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM)))
melodyTrack.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM)))

# Chord progression
for roman in PROGRESSION :
    notes = romanToChordMidi[roman]
    for note in notes:    
        chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(notes):
        if i==0:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=NOTE2))
        else:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=0))

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

midi.save(OUTPUT_FILE)
print("Generated a MIDI file:", OUTPUT_FILE)

# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
