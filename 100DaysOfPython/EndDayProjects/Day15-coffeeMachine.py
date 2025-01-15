def checkResources(MENU, resources, drink_choice):
    # Check if there is enough ingredients to make the desired drink
    # if there is, then make it and deduct from resource pool
    # else dont make
    
    valid_resources_string = "Sorry there is not enough "
    valid_resources = True
    
    for ingredient in MENU[drink_choice]["ingredients"]:
        if MENU[drink_choice]["ingredients"][ingredient] > resources[ingredient]:
            valid_resources = False
            valid_resources_string += ingredient
            break
        else:
            resources[ingredient] -= MENU[drink_choice]["ingredients"][ingredient]

    return [resources, valid_resources, valid_resources_string]


def checkFunds(MENU, resources, drink_choice, in_money):
    # Check if money inserted to coffee machine is enough.
    # If it is enough, give drink, change (if applicable), and add $ to profit
    # else, return it all
    
    
    if in_money >= MENU[drink_choice]["cost"]:
        drink_out = True
        out_money = round(in_money - MENU[drink_choice]["cost"], 2)
        resources["money"] += MENU[drink_choice]["cost"]
    else:
        drink_out = False
        out_money = round(in_money, 2)
    
    return [resources, out_money, drink_out]


def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    drink_options = ["espresso", "latte", "cappuccino"]
    
    while True:
        drink_choice = input("What would you like to like? (espresso/latte/cappuccino): ").lower()
        
        if drink_choice in drink_options: # Start making drink and asking for funds
            [resources, valid_resources, valid_resources_string] = checkResources(MENU, resources, drink_choice)
            if not valid_resources:
                print(valid_resources_string)
            else:
                print("Please insert coins.")
                in_money = 0.25 * int(input("Enter quarters: "))
                in_money += 0.10 * int(input("Enter dimes: "))
                in_money += 0.05 * int(input("Enter nickles: "))
                in_money += 0.01 * int(input("Enter pennies: "))

                [resources, out_money, drink_out] = checkFunds(MENU, resources, drink_choice, in_money)

                if drink_out == True:
                    print(f"Here is your {drink_choice}!\n")
                    if out_money > 0:
                        print(f"Here is your change: ${out_money}")
                else:
                    print(f"That is not enough, returning money: ${in_money}")
        
        elif drink_choice == "off": # End program
            print("Shutting down...")
            break
        
        elif drink_choice == "report": # show resources
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
                
        else: # Ensure input is valid
            print("Not a valid option\n")


if __name__ in "__main__":
    main()
