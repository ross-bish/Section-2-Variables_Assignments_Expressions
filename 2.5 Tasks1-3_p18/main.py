# ----------------
# Tasks 1-3 , p18
# Date: 27/9/22
# ----------------


# Task 1
age = 16
# why won't this work?
#print(age + "What a great age")
print(str(age) + " What a great age")

'''
NOTE: 
We can't concatenate integers and strings. We get the follwoing error message:

TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# However, Using a comma ' , ' we can combine both together with a space!
print(age, "What a great age")

# ---------------------------------------------------

# Task 2
# Add comments to explain what code is doing

num1 = float(5)
num2 = float(2)

sum = num1 + num2
difference = num1 - num2
product = num1 * num2

print(sum)
print(difference)
print(product)

# --------------------------------------------------

# Task 3
# Add comments to explain what code is doing

firstNumber = float(input("Enter a decimal number: "))    #
secondNumber = float(input("Enter a decimal number: "))   # 

average = (firstNumber + secondNumber) / 2    #
modulus = firstNumber % secondNumber          #   
powerOf = firstNumber ** secondNumber         #

print(average)
print(modulus)
print(powerOf)