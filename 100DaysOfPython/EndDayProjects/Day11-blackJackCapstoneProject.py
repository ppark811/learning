import random
from IPython import get_ipython

LOGO = """
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P" 
          _____                                   
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
"""

def gameStatus(player_cards, computer_cards, player_status, player_sum, computer_sum):
    end = "end"
    if player_status == "over":
        print("\nYou lose")
        showCards(player_cards, computer_cards, end)
    elif player_status == "21":
        print("\nYou win!")
        showCards(player_cards, computer_cards, end)
    else:
        if player_sum > computer_sum:
            print("\nYou win!")
            showCards(player_cards, computer_cards, end)
        elif player_sum < computer_sum:
            print("\nYou lose")
            showCards(player_cards, computer_cards, end)
        else:
            print("\nTIE! How rare")
            showCards(player_cards, computer_cards, end)
            

def checkCards(player_cards, computer_cards):
    # check card sum and position status
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)
    
    # player
    if player_sum > 21:
        player_status = "over"
    elif player_sum < 21:
        player_status = "under"
    else:
        player_status = "21"
        
    return [player_status, player_sum, computer_sum]


def showCards(player_cards, computer_cards, end = ""):
    # Show player cards and one computer card
    print(f"Your cards: {player_cards}")
    if end == "end":
        print(f"Computer cards: {computer_cards}")
    else:
        print(f"1st computer card: {computer_cards[0]}")
        
        
def drawCard(CARDS):
    # draw card
    new_card = random.choice(CARDS)
    
    return new_card


def main():
    # Initiate game
    CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(LOGO)
    print("Welcome to Blackjack, good luck\n")
    
    # Begin game
    while True:
        player_cards = []
        computer_cards = []
        
        # Start by drawing two cards each
        for i in [1,2]:
            player_cards.append(drawCard(CARDS))
            computer_cards.append(drawCard(CARDS))
            
        # Show player cards and one computer card
        showCards(player_cards, computer_cards)
        
        # ask if player wants to draw cards
        while True:
            hit = input("Do you want another card? (y/n): ")
            if hit == "y":
                # player and computer draws cards
                player_cards.append(drawCard(CARDS))
                computer_cards.append(drawCard(CARDS))
                showCards(player_cards, computer_cards)
            else:
                for i in range(0, player_cards.count(11)):
                    if 11 in player_cards:
                        ace_card_choice = input("Do you want to set your ace as 11 or 1?: (11/1): ")
                        if ace_card_choice == "1":
                            player_cards[player_cards.index(11)] = 1   
                break
            
        # Grab card sums and status of each player
        [player_status, player_sum, computer_sum] = checkCards(player_cards, computer_cards)
        
        # Check status of game
        gameStatus(player_cards, computer_cards, player_status, player_sum, computer_sum)

        go_on = input("Do you want to play again? (y/n): ")
        if go_on == "n":
            break
        else:
            get_ipython().magic("clear") #clears python console

    
if __name__ in "__main__":
    main()