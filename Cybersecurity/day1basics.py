#--VARIABLES AND BASICS--#
#MINI QS 01
name = "Maryam Imran Shah"
age = "21"
university = "Comsats"

#Type Conversion
print (int(age))
#Simple Print 
print (university)
print (name)
#Using f 
print(f"My name is {name}.I am {int(age)} years old. I study at {university}.")
#print statement worked with and without type conversion incase of f. 

#MINI QS 02 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# need to use conversion from string to int or else i got an error

sum = a+b
multiply = a*b
divide= a/b
subract = a-b

print ("Sum ",sum)
print ("Multiplication: ",multiply)
print ("Division: ",divide)
print ("Subraction: ",subract)

#MINI QS 03 
print("Area Calculation")
radius = int(input("Enter your radius: "))
area = 3.14 * radius **2

print("The area of your Circle is" ,area)

#--ASSIGNMENT OPERATORS & STRING OPERATIONS#
#MINI QS 01 
name = input("Enter your name: ")
lastname = input("Enter last name: ")
print ("String Operations")

print("Total characters: ", len(name))
print("Uppercase: ", name.upper())
print ("Lowercase: ", name.lower())
print("Full Name:" , name + " " + lastname)
print ("Nickname: ", name[0:2]+ ""+ lastname[-3:-1])
#indexing of lastname starts from smaller to bigger 

#MINI QS 02
word = "Artificial"

print(word[0])
print(word[6])
print(word[0:5])
print(word[-4:])
# to include last index use it the way above because last index is excluded in normal way[-4:-1]

#MINI QS 03 
name = "Maryam"
age = 21
print("Name",name, "\nAge",age)
print("Name\tAge\n",name,"\t",age)
# /n for vertical spacing /t for horizontal spacing 
# the give below is the way to write right column spacing
print(f"Name\tAge\n{name}\t{age}")


#--COMPARISON OPERAATORS & BOOLEAN VALUES--#
#MINI QS 01
age = 57
print(age > 66)
print (age < 88)
print (age>=11)
print(age<=99)
print(age == 57)
print (age != 57)

#MINI QS 02
a = int(input("Enter a number of your choice: "))
b = int(input("Enter a second number of your choice: "))
print("Is a greater than b: ", a>b )
print("Is b greater than equal to a: ", b>=a)
print("Is a and b equal ", a==b)

#--LOGICAL OPERATORS & IF/ELSE STATEMENTS--#
#MINI QS 01 
name = input("Enter name of student 01: ")
name2 = input("Enter name of student 02: ")
age = int(input("Enter age of student 01: "))
age2= int(input("Enter age of student 02: "))
print("COMPARISON OF STUDENTS")
print(f"{name} is older than {name2} ", age>age2)
print(f"{name} is older than {name2} and is at legal age", age>age2 and age>=18)
print(f"{name} is younger than {name2} and is not at legal age", age<age2 and  not  age >= 18)

#MINI QS 02
if  not age2>=18:
    print(name2, "is Not an Adult!")
else:
    print(name2, "is an Adult")






