def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
                leap = 1
            else:
                print("Not a leap year")
                leap = 0
        else:
            print("Leap year")
            leap = 1
    else:
        print("Not a leap year")
        leap = 0
    return leap
    

# TODO: add more code in this function
def daysInMonths(years, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = isLeap(year)
    days = monthDays[month - 1] + leap
    return days
    
    
year = int(input("enter a year: "))
month = int(input("enter a month as a number: "))
days = daysInMonths(year, month)

print(f"\nThere are {days} in {year}, {month}")
