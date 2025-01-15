year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year")
        else:
            print("Not a leap year")
    else:
        print("Is a leap year")
else:
    print("Not a leap year")