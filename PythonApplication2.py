print("welcome user to BMI calculator ")
height=float(input("enter your heigh in m:"))
weight=float(input("enter your weight in kg:"))
print("_________________________________________________________________________________________________________")
BMI=weight/(height**2)
bmi=round(BMI,2)

if BMI>=35:
    print(f"Your BMI is {bmi}, you are clinically obese")
elif BMI>=30:
    print(f"Your BMI is {bmi}, you are obese")
elif BMI>=25:
    print(f"Your BMI is {bmi}, you are overweight")
elif BMI>=18.5:
    print(f"Your BMI is {bmi} , you have a normal weight")
else:
    print(f"Your BMI is {bmi} , you are under weight ")
print("__________________________________________________________________________________________________________")    