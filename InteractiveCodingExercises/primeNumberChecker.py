def primechecker(number):
    i = number
    divisible = []
    primetrue = [number, 1]

    if number == 1:
        print(f"{number} is a prime number")
        exit()

    for x in range(0, i):
        if  number % i == 0:
            divisible.append(i)
        i -= 1

    if divisible == primetrue:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


n = int(input("Enter a integer to check: "))
primechecker(number=n)
