import random

transition_matrix = {
    "C4": {"D4": 0.4, "E4": 0.3, "G4": 0.3},
    "D4": {"E4": 0.35, "F4": 0.35, "C4": 0.3},
    "E4": {"F4": 0.4, "G4": 0.3, "C4": 0.3},
    "F4": {"G4": 0.4, "A4": 0.3, "C4": 0.3},
    "G4": {"C4": 0.4, "C5": 0.4, "A4": 0.2},
    "A4": {"B4": 0.5, "C5": 0.3, "F4": 0.2},
    "B4": {"C5": 0.6, "G4": 0.4},
    "C5": {"D5": 0.4, "E5": 0.3, "G4": 0.3},
    "D5": {"E5": 0.4, "F5": 0.3, "C4": 0.3},
    "F5": {"G5": 0.4, "A5": 0.3, "C5": 0.3},
    "G5": {"A5": 0.4, "C6": 0.3, "E5": 0.3},
}

def getNextNote(currentNote):
    if currentNote not in transition_matrix:
        nextNote = "C4"
    else:
        candidates = list(transition_matrix[currentNote].keys())
        probs = list(transition_matrix[currentNote].values())
        nextNote = random.choices(candidates, probs)[0]
    return nextNote

melody = []
currentNote = "C4"
melody.append(currentNote)

# 4 beats, 2 measures
for _ in range(7):
    nextNote = getNextNote(currentNote)
    melody.append(nextNote)
    currentNote = nextNote

print(melody)
# print(", ".join(melody))
