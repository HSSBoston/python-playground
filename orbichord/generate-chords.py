from music21.scale import MajorScale
from orbichord.generator import Generator

scale = MajorScale('D')  # D major

chord_generator = Generator(
    pitches=scale.getPitches('D4', 'C#5'),
    dimension=3,
    select=lambda chord: chord.isTriad()
)

chords = list(chord_generator.run())