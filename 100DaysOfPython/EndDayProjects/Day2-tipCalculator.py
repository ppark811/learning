print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? "))
tipPercentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
if tipPercentage not in [0.1, 0.12, 0.15]:
    print("Not a valid tip percentage option, ending script")
    exit()
totalPeople = int(input("How many people to split the bill?" ))

billAndTip = totalBill * (1+tipPercentage)
splitAmount = round(billAndTip/totalPeople, 2)

print(f"Each person should pay: {splitAmount}")