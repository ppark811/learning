print("Welcome to the Band Name Generator.")

while True:
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")

    print("Your band name could be " + city + " " + pet)

    go_on = input("Want to try again? (y/n)\n")

    if go_on == "y":
        continue
    elif go_on == "n":
        print("End of Band Name Generator")
        break
    else:
        print("Not a valid entry, restarting program")
