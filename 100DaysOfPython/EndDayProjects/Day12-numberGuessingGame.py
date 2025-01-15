import random


def checkGuess(guess, solution):
    
    win = False
    if guess > solution:
        print("Too high")
    elif guess < solution:
        print("Too low")
    else:
        print("You win!")
        win = True
    return win
        

def setDifficulty():
    difficulty = input("Choose a difficulty - 'easy' or 'hard': ")
    if difficulty == "easy":
        attempt = 10
    elif difficulty == "hard":
        attempt = 5
    else:
        print("Not a valid option")
        exit()
    return [difficulty, attempt]


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    solution = random.randint(1,100)

    [difficulty, attempt] = setDifficulty()    
    
    while True:
        
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        
        win = checkGuess(guess, solution)
        
        attempt -= 1

        if win == True:
            break
        if attempt == 0:
            print("You've run out of guesses, you lose")
            print(f"The number was {solution}")
            break


if __name__ in "__main__":
    main()
    