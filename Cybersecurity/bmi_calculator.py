#This is just basic implementaion of Python Foundation for Day 01

print("======= BMI CALCULATOR =======")
name = input("Enter your full name: ")
if len(name)==0:
    print("Name cannot be empty.")
    exit()
elif not name.replace(" ", "").isalpha():
    print("Invalid input!")
    exit()
age = float(input("Enter your age (in years): "))
if age <=0:
    print("Age cannot be zero or negative.")
    exit()

weight_units= int(input("Choose weight units: \n1.kg\n2.lb: "))
weight=float(input("Enter your weight: "))
if weight <=0:
    print("Weight cannot be zero or negative.")
    exit()
if weight_units == 1:
    weight = weight
elif weight_units ==2:
    weight = weight * 0.453592
else:
    print("Invalid option!")
    exit()
height = float(input("Enter your height(in meters) :"))
if height <=0:
    print("Height cxannot be zero or negative.")
    exit()

bmi = weight/height**2
print ("=========BMI REPORT==========")
print(f"Name:\t", name.upper(),f"\nAge:\t{age}\nWeight:\t{weight}\nHeight:\t{height}\nBMI:\t{bmi}")
if bmi < 18.5:
    print("You are Underweight.")
elif bmi >=18.5 and bmi <=24.9 :
    print("You are Normal Weight.")
elif bmi>=25 and bmi <=29:
     print("You are over weight.")
else:
    print("You are obese.")