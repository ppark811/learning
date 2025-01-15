import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_alphabet = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

continue_check = True

while continue_check:
    word = input("enter a word: ").upper()
    
    try:
        result = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters are accepted")
    else:
        print(result)
        continue_check = False
