import mido, random
from mido import Message, MidiFile, MidiTrack, MetaMessage
from music21 import *
from pprint import pprint

KEY_CHOICE = "a"
# KEY_CHOICE = "C"
PROGRESSION = ["I", "IV", "VII", "I", "VI", "II", "V", "I"]
# PROGRESSION = ["I", "IV", "V", "I"]
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
    rn1 = roman.RomanNumeral("I", scale)
    rn2 = roman.RomanNumeral("ii", scale)
    rn4 = roman.RomanNumeral("IV", scale)
    rn5 = roman.RomanNumeral("V", scale)
    rn6 = roman.RomanNumeral("vi", scale)
    rn7 = roman.RomanNumeral("viio", scale)

    rn17 = roman.RomanNumeral("I7", scale)
    rn27 = roman.RomanNumeral("ii7", scale)
    rn47 = roman.RomanNumeral("IV7", scale)
    rn57 = roman.RomanNumeral("V7", scale)
    rn67 = roman.RomanNumeral("vi7", scale)
    rn77 = roman.RomanNumeral("viio7", scale)
else:
    rn1 = roman.RomanNumeral("i", scale)
    rn2 = roman.RomanNumeral("iio", scale)
    rn4 = roman.RomanNumeral("iv", scale)
    rn5 = roman.RomanNumeral("v", scale)
    rn6 = roman.RomanNumeral("VI", scale)
    rn7 = roman.RomanNumeral("VII", scale)

    rn17 = roman.RomanNumeral("i7", scale)
    rn27 = roman.RomanNumeral("iio7", scale)
    rn47 = roman.RomanNumeral("iv7", scale)
    rn57 = roman.RomanNumeral("v7", scale)
    rn67 = roman.RomanNumeral("VI7", scale)
    rn77 = roman.RomanNumeral("VII7", scale)

romanToChord = {
    "I":  rn1,
    "II": rn2,
    "IV": rn4,
    "V":  rn5,
    "VI": rn6,
    "VII":rn7
    }
# pprint(romanToChord)

romanTo7thChord = {
    "I":  rn17,
    "II": rn27,
    "IV": rn47,
    "V":  rn57,
    "VI": rn67,
    "VII":rn77
    }
# pprint(romanTo7thChord)

romanToChordTones = {
    "I":  [p.nameWithOctave for p in rn1.pitches],
    "II": [p.nameWithOctave for p in rn2.pitches],
    "IV": [p.nameWithOctave for p in rn4.pitches],
    "V":  [p.nameWithOctave for p in rn5.pitches],
    "VI": [p.nameWithOctave for p in rn6.pitches],
    "VII":[p.nameWithOctave for p in rn7.pitches],    
    }
pprint(romanToChordTones)

romanTo7thChordTones = {
    "I":  [p.nameWithOctave for p in rn17.pitches],
    "II": [p.nameWithOctave for p in rn27.pitches],
    "IV": [p.nameWithOctave for p in rn47.pitches],
    "V":  [p.nameWithOctave for p in rn57.pitches],
    "VI": [p.nameWithOctave for p in rn67.pitches],
    "VII":[p.nameWithOctave for p in rn77.pitches],    
    }
pprint(romanTo7thChordTones)

romanToChordTonesMidi = {
    "I":  [p.midi for p in rn1.pitches],
    "II": [p.midi for p in rn2.pitches],
    "IV": [p.midi for p in rn4.pitches],
    "V":  [p.midi for p in rn5.pitches],
    "VI": [p.midi for p in rn6.pitches],
    "VII":[p.midi for p in rn7.pitches],
    }
pprint(romanToChordTonesMidi)

romanTo7thChordTonesMidi = {
    "I":  [p.midi for p in rn17.pitches],
    "II": [p.midi for p in rn27.pitches],
    "IV": [p.midi for p in rn47.pitches],
    "V":  [p.midi for p in rn57.pitches],
    "VI": [p.midi for p in rn67.pitches],
    "VII":[p.midi for p in rn77.pitches],
    }
pprint(romanTo7thChordTonesMidi)

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
    chordTonesMidi = romanToChordTonesMidi[roman]
    for note in chordTonesMidi:    
        chordTrack.append(Message('note_on', note=note, velocity=60, time=0))
    for i, note in enumerate(chordTonesMidi):
        if i==0:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=NOTE2))
        else:
            chordTrack.append(Message('note_off', note=note, velocity=60, time=0))

# Melody
#   Chord notes at 70% and scale notes at 30%
#   quarter and 8th notes at random
def melodyWithTriadRandamized():
    for roman in PROGRESSION:
        chordTonesMidi = romanToChordMidi[roman]
        remainingTicks = NOTE2
        
        while remainingTicks > 0:
            duration = random.choice([NOTE4, NOTE8])
            if remainingTicks - duration < 0:
                duration = remainingTicks        
            
            if random.random() < 0.7:
                note = random.choice(chordTonesMidi)
            else:
                note = random.choice(scaleMidi)
                
            melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
            melodyTrack.append(Message('note_off', note=note, velocity=80, time=duration))
            
            remainingTicks -= duration

# Melody
#   Chord notes at 70% and scale notes at 30%
#   quarter and 8th notes at random
def melodyWith7thChordRandamized():
    for roman in PROGRESSION:
        chordTonesMidi = romanTo7thChordTonesMidi[roman]
        remainingTicks = NOTE2
        
        while remainingTicks > 0:
            duration = random.choice([NOTE4, NOTE8])
            if remainingTicks - duration < 0:
                duration = remainingTicks        
            
            if random.random() < 0.7:
                note = random.choice(chordTonesMidi)
            else:
                note = random.choice(scaleMidi)
                
            melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
            melodyTrack.append(Message('note_off', note=note, velocity=80, time=duration))
            
            remainingTicks -= duration

# Melody
#   degreeSeq: e.g. [3, 5, 1, 7]
#   quarter and 8th notes at random
def melodyWithChordDegrees(degreeSeq):
    for roman in PROGRESSION:
        chordTonesMidi = romanTo7thChordTonesMidi[roman]        
        for degNum in degreeSeq:
            if degNum == 1:
                note = chordTonesMidi[0]
                if random.random() > 0.9:
                    note += 12
                if random.random() > 0.9:
                    note -= 12
            elif degNum == 3:
                note = chordTonesMidi[1]
                if random.random() > 0.9:
                    note += 12
                if random.random() > 0.9:
                    note -= 12
            elif degNum == 5:
                note = chordTonesMidi[2]
                if random.random() > 0.9:
                    note += 12
                if random.random() > 0.9:
                    note -= 12
            elif degNum == 7:
                note = chordTonesMidi[3]
                if random.random() > 0.9:
                    note += 12
                if random.random() > 0.9:
                    note -= 12
            melodyTrack.append(Message('note_on', note=note, velocity=80, time=0))
            melodyTrack.append(Message('note_off', note=note, velocity=80, time=NOTE8))

if __name__ == "__main__":
#     melodyWithChordDegrees([3,5,1,7])
    melodyWithChordDegrees([3,1,5,7])
    
    midi.save(OUTPUT_FILE)
    print("Generated a MIDI file:", OUTPUT_FILE)




# midi = MidiFile('random-song.mid')
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)
