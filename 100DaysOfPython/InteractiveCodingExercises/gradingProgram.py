studentScores = {"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}

studentGrades = {}

for student in studentScores:
    if studentScores[student] > 90:
        studentGrades[student] = "Outstanding"
    elif studentScores[student] > 80:
        studentGrades[student] = "Exceeds Expectations"
    elif studentScores[student] > 70:
        studentGrades[student] = "Acceptable"
    else:
        studentGrades[student] = "Fail"

print(studentGrades)
