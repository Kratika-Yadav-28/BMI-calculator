#BMI CALCULATOR
print("BMI calculator")
print("Lets see how fit you are........")
Weight = float(input("Enter your weight in kg : "))
Height = float(input("Enter your height in m : "))

def BMI(height, weight):
    return round((weight / height**2),2)

BodyMassIndex = BMI(Height,Weight)
print("Your Body Mass Index is : ",BodyMassIndex)

if (BodyMassIndex <= 18.5):
    print("You are underweight.")
elif (18.5 < BodyMassIndex <= 24.9):
    print("Your weight is normal.")
elif (25 < BodyMassIndex <= 29.29):
    print("You are overweight.")
else:
    print("You are obese.")
