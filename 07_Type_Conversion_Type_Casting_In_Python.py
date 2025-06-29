# Type Conversion and Type Casting in Python

#  Type Conversion (or Type Casting) means changing the **data type** of a value or variable.
#  Python provides built-in functions like `int()`, `float()`, `str()`, `list()`, etc. for type casting.
#  It's useful when you need to perform operations that require values to be in a specific type.

# ----------------------------------------------
# Checking the data type using type()
x = 4
print(x, type(x))  # Output: 4 <class 'int'>

y = 3.3
print(y, type(y))  # Output: 3.3 <class 'float'>

marks = {"name": "Yasir"}
print(marks, type(marks))  # Output: {'name': 'Yasir'} <class 'dict'>

# ----------------------------------------------
# Type Conversion Example (String to String Concatenation)
x = "100"
y = "200"
z = x + y
print(z)  # Output: 100200 (string concatenation)

# Now let's convert the strings to integers for numeric addition
x = int("100")
y = int("200")
z = x + y
print(z)  # Output: 300

# Invalid conversion (string contains non-numeric characters)
# This will raise a ValueError
# x = int("100abc")
# y = int("200")
# z = x + y
# print(z)

# Another invalid case: converting float-string directly to int
# x = int("100.4")  # Will raise ValueError
# y = int("200")
# z = x + y
# print(z)

# Correct way: Convert to float first
x = float("100.4")
y = float("200")
z = x + y
print(z)  # Output: 300.4

# ----------------------------------------------
#  Summary of Type Casting Functions in Python:
# int()    → Converts to integer (whole number)
# float()  → Converts to decimal number
# str()    → Converts to string
# list()   → Converts to list
# dict()   → Converts to dictionary (with valid format)
# bool()   → Converts to True or False
