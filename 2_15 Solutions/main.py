# -------------------
# Solutions - Assessment 1 - Intro to Python
# Date: 28/9/22
# -------------------

#Q1
# Write a program to display the statement "I am studying Computer Science"
print("I am studying Computer Science\n")

# Q2
# Write a program to concatenate two strings "Computer Science" AND "101"
print("Computer Science" + " 101\n")

# Q3
# Write a program to calculate each of the following:
# divide 40 by 11
divide = 40 / 11
print(divide)
# find the remainder when 40 is divided by 11
modulus = 40 % 11
print(modulus)
# calculate 2 to the power of 10
powerOf = 2 ** 10
print(powerOf)
print()

# Q4
# # Ask the user for their First Name and then ask for their Surname and display the outputs as:
firstName = input("Enter First Name: ") # collects user input
surname = input("Enter Surname: ")      # collects user input

print("Hello", firstName, surname)

# Add comments to the lines that collect the user input



# Q5
# There are 2.204 pounds in a kilogram. 
# Ask the user to enter a weight in kilograms and convert it to pounds. 
kilos = float(input("Enter weight in kgs: "))

pounds = kilos * 2.204                      # conversion takes place here
print("Your weight in pounds = ", pounds)

# Add comments to the line where the conversion takes place.


# Q6
# Write a program to ask the user to enter the radius of a circle and calculate the circumferance of a circle.
r = float(input("Enter radius: "))
pi = 3.14159

circumference = 2 * pi * r
print("Circumference = ", circumference)


# Q7
# Write a progam which asks the user to enter two floating point numbers num1 and num2 and prints the sum and product rounded to 2 decimal places.

num1 = float(input("Enter decimal number 1: "))
num2 = float(input("Enter decimal number 2: "))

sum = num1 + num2
sum = round(sum, 2)          # round to 2 decimal places
product = num1 * num2
product = round(product, 2)  # round to 2 decimal places

print("Sum is", sum)
print("Product is", product)
# Add comments to the lines where the rounding takes place
