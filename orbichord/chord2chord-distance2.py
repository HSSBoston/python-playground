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
startOrderedPitches = []
for degree in range(1, 8):
    for p in start.pitches:
        pitchDegree = scale.getScaleDegreeFromPitch(
            p, comparisonAttribute="pitchClass")
        if pitchDegree == degree:
            startOrderedPitches.append(p)
print(startOrderedPitches)

# Apply the voice-leading movement to each pitch
targetPitches = []
for p, steps in zip(startOrderedPitches, movement):
    if steps == 0:
        newPitch = p
    else:
        direction = Direction.ASCENDING if steps > 0 else Direction.DESCENDING
        newPitch = scale.nextPitch(p, direction=direction, stepSize=abs(steps))
    targetPitches.append(newPitch)

voicingResult = Chord(targetPitches)
assert sorted(voicingResult.pitchClasses) == sorted(target.pitchClasses)

print("Chord:",     voicingResult.pitches)
print("Root:",      voicingResult.root().name)
print("Quality:",   voicingResult.quality)
print("Inversion:", voicingResult.inversionText())

