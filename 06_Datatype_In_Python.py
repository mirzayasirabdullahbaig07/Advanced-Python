#  Data Types in Python

# ➤ Data types specify what kind of value a variable holds.
# ➤ They also determine what operations (mathematical, relational, logical) can be performed on that value.

# ----------------------------------------------------------
# Main Data Types in Python with Examples
# ----------------------------------------------------------

# 1. Numeric Types → int, float, complex

# Integer (whole number)
num1 = 10
print("Integer:", num1)

# Float (decimal number)
num2 = 3.14
print("Float:", num2)

# Complex number (real + imaginary)
num3 = 2 + 3j
print("Complex:", num3)

# 2. Boolean → True or False
is_active = True
print("Boolean:", is_active)

# 3. String → Text enclosed in quotes
message = "Hello, Yasir!"
print("String:", message)

# 4. List → Ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# 5. Tuple → Ordered, unchangeable (immutable), allows duplicates
coordinates = (10, 20)
print("Tuple:", coordinates)

# 6. Set → Unordered, no duplicates
unique_numbers = {1, 2, 3, 3, 2}
print("Set:", unique_numbers)  # Output: {1, 2, 3}

# 7. Dictionary → Key-value pairs, unordered (Python 3.6+ maintains insertion order)
person = {"name": "Yasir", "age": 24}
print("Dictionary:", person)

# ----------------------------------------------------------
# Summary of Python Data Types:

# int       → Whole numbers
# float     → Decimal numbers
# complex   → Numbers with real + imaginary part
# bool      → True or False
# str       → Text
# list      → Ordered, changeable, [ ]
# tuple     → Ordered, unchangeable, ( )
# set       → Unordered, unique values, { }
# dict      → Key-value pairs, {key: value}
