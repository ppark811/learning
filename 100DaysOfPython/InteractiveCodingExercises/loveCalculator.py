print("The Love Calculator is calculating your score...")
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")

combinedName = name1 + name2
lowerName = combinedName.lower()

tCounter = lowerName.count("t")
rCounter = lowerName.count("r")
uCounter = lowerName.count("u")
eCounter = lowerName.count("e")
trueSum = tCounter + rCounter + uCounter + eCounter

lCounter = lowerName.count("l")
oCounter = lowerName.count("o")
vCounter = lowerName.count("v")
loveSum = lCounter + oCounter + vCounter + eCounter

print(f"T occurs {tCounter} times")
print(f"R occurs {rCounter} times")
print(f"U occurs {uCounter} times")
print(f"E occurs {eCounter} times")
print(f"Total = {trueSum}")

print(f"T occurs {lCounter} times")
print(f"R occurs {oCounter} times")
print(f"U occurs {vCounter} times")
print(f"E occurs {eCounter} times")
print(f"Total = {loveSum}")

trueLoveSum = int(str(trueSum) + str(loveSum))

if trueLoveSum < 10 or 90 < trueLoveSum:
    print(f"Your score is {trueLoveSum}, you go together like coke and mentos")
elif 40 < trueLoveSum or trueLoveSum < 50:
    print(f"Your score is {trueLoveSum}, you are alright together:")
else:
    print(f"Love Score = {trueLoveSum}")
