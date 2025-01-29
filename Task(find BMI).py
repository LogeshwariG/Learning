#enter your height in meters
height = float(input())

#enter your weight in Kilograms
weight = int(input())

BMI = weight + (height * height)


if BMI < 25:
    print(f"Your BMI is {BMI},you are underweight")
elif BMI >= 25 or BMI < 30:
    print(f"Your BMI is {BMI},you have a normal weight")
elif BMI >= 30 or BMI < 35:
    print(f"Your BMI is {BMI},you are obese")
else:
    print(f"Your BMI is {BMI},you are Clinically obese")
