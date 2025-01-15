def checkResources(drink_choice, MENU, resources):

    valid_resources_string = "Sorry there is not enough "
    valid_resources = True
    for ingredient in MENU[drink_choice]["ingredients"]:
        if MENU[drink_choice]["ingredients"][ingredient] > resources[ingredient]:
            valid_resources = False
            valid_resources_string += ingredient
            break
        else:
            resources[ingredient] -= MENU[drink_choice]["ingredients"][ingredient]

    return [valid_resources, valid_resources_string, resources]


def checkFunds(in_money):
    funds = 0
    #TODO fill this part out
    return funds

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
        if drink_choice in drink_options:
            [valid_resources, valid_resources_string, resources] = checkResources(drink_choice, MENU, resources)
            if not valid_resources:
                print(valid_resources_string)
            else:
                quarters = 0.25 * int(input("Enter quarters: "))
                dimes = 0.10 * int(input("Enter dimes: "))
                nickles = 0.05 * int(input("Enter nickles: "))
                pennies = 0.01 * int(input("Enter pennies: "))

                in_money = quarters + dimes + nickles + pennies

                funds = checkFunds(in_money)

                # TODO ask for money and process it to see if it is enough
                    #TODO elif not enough, return money


                    #TODO if enough or over amount, give drink and refund change
                    print(f"Here is your {drink_choice}!\n")
        
        # This part is only glitching out because the indent above, dont worry about it
        elif drink_choice == "off":
            print("Shutting down...")
            break
        elif drink_choice == "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
        else:
            print("Not a valid option\n")


if __name__ in "__main__":
    main()
