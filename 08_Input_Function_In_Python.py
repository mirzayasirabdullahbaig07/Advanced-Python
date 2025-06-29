#  Input Function in Python

#  The input() function is used to take **user input**.
#  Whatever the user types is stored as a **string**, by default.

#  Simple Example
x = input("Enter your name: ")
print("You entered:", x)

# ----------------------------------------------
#  User Input Example — Asking for name, gender, and age

name = input("Enter your name: ")
gender = input("Enter your gender: ")
age = int(input("Enter your age: "))  # Convert input from string to integer using int()

#  Displaying user input using f-string
print(f"My name is {name}, my age is {age}, and my gender is {gender}")

# ----------------------------------------------
#  Notes:
# - All input values are stored as strings by default.
# - Use `int()`, `float()`, or `bool()` to convert them if needed.
#   Example: age = int(input("Enter your age: "))
