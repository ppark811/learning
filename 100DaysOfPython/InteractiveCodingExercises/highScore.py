studentScores = [78,65,89,86,55,91,64,89]

topScore = studentScores[0]
for score in studentScores:
    if topScore < score:
        topScore = score
    else:
        pass

print(f"The highest score is {topScore}")