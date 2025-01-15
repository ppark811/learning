import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Random word selection
wordList = ["aardvark", "baboon", "camel","elephant","soju","dog","samoyed"]
chosenWord = random.choice(wordList)

#print(chosenWord)

# Create blanks
display = []
for n in range(len(chosenWord)):
    display.append("_")

lives = 6

while display != list(chosenWord):

    print(stages[lives])
    print("".join(display))
    # Take user input
    guess = input("Enter your letter guess: ").lower()

    # Check if guess is in word and place letter into correct placement
    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter

    if guess not in list(chosenWord):
        lives -= 1
        if lives == 0:
            print("You lose!")
            print(f"\nWord was {chosenWord}")
            break

    if display == list(chosenWord):
        print("You won!")
        print(chosenWord)
