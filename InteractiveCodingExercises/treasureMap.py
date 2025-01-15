line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
treasureMap = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter a position using 'A,B,C' for horizontal position and '1,2,3' for vertical.\n e.g B3\n->")

letter = position[0].lower()
horiPos = int(position[1]) - 1

abc = ["a", "b", "c"]
vertPos = abc.index(letter)

#This is not as clean, using .index() method is much cleaner
# if vertPos == "A":
#     vertPos = 0
# elif vertPos == "B":
#     vertPos = 1
# elif vertPos == "C":
#     vertPos = 2
# else:
#     print("Not a valid entry")
#     exit()

treasureMap[horiPos][vertPos] = "X"
print(f"{line1}\n{line2},\n {line3}")
