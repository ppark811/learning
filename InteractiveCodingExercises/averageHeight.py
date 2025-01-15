studentHeights = [156, 178, 165, 171, 187]

#force all values to be integers
for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])

totalHeight = 0
for height in studentHeights:
    totalHeight += height
print(totalHeight)

numberOfStudents = 0
for n in studentHeights:
    numberOfStudents += 1
print(numberOfStudents)

averageHeight = round(totalHeight/numberOfStudents)

print(averageHeight)
