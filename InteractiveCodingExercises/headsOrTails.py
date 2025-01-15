#Random module practice

import random

print("This is a virutal coin toss")

face = random.randint(0,1)

if face == 1:
    print("Heads")
elif face == 0:
    print("Tails")
else:
    print("random module failed")
