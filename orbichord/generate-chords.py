from music21.scale import MajorScale
from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure
from orbichord.identify import chordPitchNames

scale = MajorScale("C")

# Generate an orbifold 
chordGen = Generator(
    pitches=scale.getPitches("C", "B"),
    dimension=3,
    select=lambda chord: chord.isTriad() )

#chords = list(chord_generator.run())

for chord in chordGen.run():
    print(chordSymbolFigure(chord, inversion=0), chordPitchNames(chord))

