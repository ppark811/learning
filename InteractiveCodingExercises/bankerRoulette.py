import random

nameString = "Angela, Ben, Jenny, Michael, Chloe"
names = nameString.split(", ")

payName = names[random.randint(0, len(names))-1]

print(f"{payName} is going to buy the meal today!")
