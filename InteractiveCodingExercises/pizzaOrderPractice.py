print("Thank you for choosing Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
addPepperoni = input("Do you want pepperoni? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill += 15
    if addPepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if addPepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    if addPepperoni == "Y":
        bill += 3

else:
    print("Not a valid size")

if extraCheese == "Y":
    bill += 1

print(f"\nYour Final bill is: ${int(bill)}")
