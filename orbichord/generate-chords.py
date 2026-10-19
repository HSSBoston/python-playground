from music21.scale import MajorScale
from orbichord.generator import Generator

scale = MajorScale("C")

# Generate an orbifold 
chord_generator = Generator(
    pitches=scale.getPitches("C", "B"),
    dimension=3,
    select=lambda chord: chord.isTriad() )

chords = list(chord_generator.run())
print(chords)
