from music21.chord import Chord
from music21.scale import MajorScale, Direction
from numpy.linalg import norm
from orbichord.chordinate import EfficientVoiceLeading

scale = MajorScale("C")

start  = Chord("C4 E4 G4")
target = Chord("G4 B4 D5")

vl = EfficientVoiceLeading( scale=scale,
                            metric=lambda delta: norm(delta, 1) )
movement, distance = vl(start, target)
print("Movement:", movement)
print("Distance:", distance)

# Sort starting pitches by scale degree
orderedPitches = []
for degree in range(1, 8):
    for p in start.pitches:
        pitchDegree = scale.getScaleDegreeFromPitch(
            p, comparisonAttribute="pitchClass")
        if pitchDegree == degree:
            orderedPitches.append(p)
print(orderedPitches)
# 
# 
# # Apply the voice-leading movement to each pitch
# result_pitches = []
# 
# for p, steps in zip(ordered_pitches, movement):
#     steps = int(steps)
# 
#     if steps == 0:
#         new_pitch = p
#     else:
#         direction = (
#             Direction.ASCENDING if steps > 0
#             else Direction.DESCENDING
#         )
#         new_pitch = scale.nextPitch(
#             p,
#             direction=direction,
#             stepSize=abs(steps)
#         )
# 
#     result_pitches.append(new_pitch)
# 
# # Construct the actual voiced chord
# result = Chord(result_pitches)
# 
# # Verify it has the intended target pitch classes
# assert sorted(result.pitchClasses) == sorted(target.pitchClasses)
# 
# print("Chord:", " ".join(p.nameWithOctave for p in result.pitches))
# print("Root:", result.root().name)
# print("Quality:", result.quality)
# print("Inversion:", result.inversionText())
# print("Description:",
#       f"{result.root().name} {result.quality}, "
#       f"{result.inversionText().lower()}")
