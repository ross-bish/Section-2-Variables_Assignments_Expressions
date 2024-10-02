# ----------------
# ASCII code
# Date:
# ----------------

# Add comments where necessary to describe what your code is doing.
'''
character = "A"
ascii = ord(character)   # converting "A" into a decimal value, storing value in the ascii variable
print(type(ascii))    # shows data type
print("The decimal value for the letter A is: ", ascii)

output = chr(ascii)  # converting decimal value to a letter
print(type(output))  # display data type
print("The character represented by decimal value", ascii, " is: ", output)
'''

### Practice

### V1
value = input("Enter keyboard value: ")
ascii = ord(value)
print("The decimal value of", value, "is", ascii)

### V2
name = input("Enter name: ")

for i in name:
    ascii_value = ord(i)
    print(f"The decimal value of {i} is {ascii_value}")


decimal = int(input("Enter Unicode value: "))
unicode = chr(decimal)
print("The character representation of", decimal, "is", unicode)
