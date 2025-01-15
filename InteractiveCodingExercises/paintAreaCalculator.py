import math
def paintcalc(height, width, cover):
    numberOfCans = math.ceil((height * width) / cover)
    return numberOfCans


testH = int(input("Enter test height: "))
testW = int(input("Enter test width: "))
coverage = 5

numberOfCans = paintcalc(height=testH, width=testW, cover=coverage)
print(f"You need {numberOfCans} cans of paint.")
