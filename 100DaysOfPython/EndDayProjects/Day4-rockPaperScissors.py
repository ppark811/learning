import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rockPaperScissor = [rock, paper, scissors]
yourDecision = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 or Scissors.\n"))
computerDecision = random.randint(0,2)

print(rockPaperScissor[yourDecision])
print(f"Computer Chose: \n {rockPaperScissor[computerDecision]}")

if yourDecision == computerDecision:
    print("Tie")
elif yourDecision == 0 and computerDecision == 1:
    print("You lose")
elif yourDecision == 0 and computerDecision == 2:
    print("You win")
elif yourDecision == 1 and computerDecision == 0:
    print("You win")
elif yourDecision == 1 and computerDecision == 2:
    print("You win")
elif yourDecision == 2 and computerDecision == 0:
    print("You win")
elif yourDecision == 2 and computerDecision == 1:
    print("You win")
else:
    print("game aint workin")
