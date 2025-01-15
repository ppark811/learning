# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []

# There's probably a way to do this in a nested loop

# possibleValues = [letters, numbers, symbols]
# selection = [nr_letters, nr_symbols, nr_numbers]
# for n in selection:
#     for  in range(0, values):
#         passSelection = random.randint(0, len(values) - 1)
#         easyPassword.append(values[passSelection])


for n in range(0, nr_letters):
    passLetterSelection = random.randint(0, len(letters) - 1)
    password.append(letters[passLetterSelection])
for n in range(0, nr_symbols):
    passSymbolSelection = random.randint(0, len(symbols) - 1)
    password.append(symbols[passSymbolSelection])
for n in range(0, nr_numbers):
    passNumberSelection = random.randint(0, len(numbers) - 1)
    password.append(numbers[passNumberSelection])
    #Can short

easyPassword = "".join(password)
print(f"This is the easy password: {easyPassword}, with a character length of {len(easyPassword)}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)

hardPassword = "".join(password)
print(f"This is the hard password: {hardPassword}, with a character length of {len(hardPassword)}")


## Instructor solution
#
# Easy password:
# password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#     #or shorten with this: password += random.choice(letters)

# Hard Password:
# use same method I did, generate a list then shuffle it.