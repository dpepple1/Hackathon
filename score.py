#!/usr/bin/python3
def calculateScore(score, servings):
    finalscore1 = score - min((12000*(1/score)*((servings-1)*3)), score)
    print(int(finalscore1))
    return int(finalscore1)

def calculateMealScore(chosenItems):
    total = 0
    for item in chosenItems:
        total += calculateMealScore(item[0], item[1])

    finalScore = int(total/len(chosenItems))
    return finalScore


score = 300
servings = 3
calculateScore(score,servings)

