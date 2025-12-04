import random

noteChoices = [["C", 1.5],
               ["D", 1],
               ["E", 1.2]]

def weightedChoice(choices):
    totalWeight = sum([weight for item, weight in choices])
    print(totalWeight)
    if totalWeight == 0:
        return random.choice([item for item, weight in choices])
    else:
        return random.choices([item for item, weight in choices],
                              weights=[weight for item, weight in choices],
                              k=1)

print( weightedChoice(noteChoices) )
