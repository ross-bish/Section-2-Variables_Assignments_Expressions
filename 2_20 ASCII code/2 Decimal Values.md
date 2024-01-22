# Decimal Values
The following examples are from your textbook.

## Obtaining the ASCII decimal value of a character
Let’s look at how to get the ASCII decimal value in Python of 
a single letter (e.g. the letter A)

1. Run the following in `main.py`
````py
character = "A"
ascii = ord(character)
print(type(ascii))
print("The decimal value for the letter A is: ", ascii)
````
Note that the `ord()` function takes a character and returns 
the ASCII decimal value for that character. This decimal 
value is, of course, an integer. We can show this by 
displaying the variable type using the `type()` function.

## Converting an ASCII decimal value to a character
We can take an ASCII decimal value and convert it to the 
character that it represents using the `chr()` function.

2. Add these lines to the previous script in `main.py`:
````py
output = chr(ascii)
print(type(output))
print("The character represented by decimal value", ascii, " is: ", output)
````
Note that the `chr()` function takes an ASCII decimal value 
and converts it to the character that it represents. 
It also automatically converts the variable type to a string, as we can see above.

Practise using `ord()` and `chr()` to convert the following 
characters to decimal values and back again: `E, 2, &, @`

## Challenge
👉 Now I want you to convert your name into ASCII code:
