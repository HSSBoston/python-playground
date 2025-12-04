import random

noteChoices = [["C", 1.5],
               ["D", 1],
               ["E", 1.2]]

def weightedChoice(choices):
    totalWeight = sum([w for _, w in choices])
    print(totalWeight)
    if total == 0:
        return random.choice([item for item, _ in choices])
    r = random.uniform(0, totalWeight) # random float in [0, totalWeight]
    upto = 0
    for item, weight in choices:
        if upto + weight >= r:
            return item
        upto += weight
    return choices[-1][0]

print( weightedChoice(noteChoices) )
