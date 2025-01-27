height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight/(height ** 2), 1)
#print(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif 18.5 <= BMI and BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight")
elif 25 <= BMI and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif 30 <= BMI and BMI < 30:
    print(f"Your BMI is {BMI}, you are obese")
elif BMI >= 30:
    print(f"Your BMI is {BMI}, you are clinically obese")
