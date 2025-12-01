"""Multiple
Line
Comment >:)

I can wrtite in multiple lines
and it will still be a comment"""

# integers are numbers without a decimal point (0-9 and all combinations)
# floats are numbers with a decimal point (0.01 - 9.99 and all combinations)
#char is a single character (a-z, A-Z, 0-9, !@#$%^&*()_+ etc) enclosed in ' ' or " "
#string is an array of char that can be anything enclosed in ' ' or " "
#eg symbols = "!@#$%^&*()_+", alphabet = "abcdefghijklmnopqrstuvwxyz", numbers = "0123456789", etc.
# Boolean is either True or False
#WAP (Write A Program)
#WAP to enter all kinds of variables and display them

name = "Senuk"
age = 11
grade = 7
happy = True
division = 'A'

print("My name is ", name)
print("I am ", age, " years old")
print("I am in grade ", grade)
print("I am in division ", division)
print("It is ", happy, " that I am happy")

print ("-------------------------------")
#F-String
print(f" My name is {name},\n I am {age} years old,\n I am in grade {grade} and division {division}.\n It is {happy} that I am happy.")

print ("-------------------------------")

name = input("Enter your name: ")
age = int(input(f"Enter your age {name}: ")) 
n = int(input("Enter a number: "))
text = f"We have {n} chickens."
print(text)
text = f"The price of each chicken is {n:.3f} dollars."
print(text)
buy = int(input("How many chickens do you want to buy: "))
text = f"The total price for {buy} chickens without tax is {buy * n:.2f} dollars."
tax = 0.13 * buy * n
text = f"The total price for {buy} chickens with tax is {buy * n + tax:.2f} dollars."
budget = float(input("Enter your budget: "))
text1 = f"Sorry, it is {'Expensive' if budget < (buy * n + tax) else 'Affordable'} for you."
print(text)
print(text1)
