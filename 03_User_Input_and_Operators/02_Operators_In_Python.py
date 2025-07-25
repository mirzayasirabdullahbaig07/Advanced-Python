# What are Operators?
# Operators are used to perform operations on variables and values.

# Different Types of Operators:
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators 
# Bitwise Operators

# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform mathematical operations.

# Addition (+)
a = 10 + 5
print("Addition:", a)  # Output: 15

# Subtraction (-)
b = 10 - 3
print("Subtraction:", b)  # Output: 7

# Multiplication (*)
c = 4 * 5
print("Multiplication:", c)  # Output: 20

# Division (/)
d = 10 / 2
print("Division:", d)  # Output: 5.0

# Modulus (%)
# Modulus gives the remainder of a division
e = 10 % 3
print("10 % 3 =", e)  # Output: 1

f = 5 % 10
print("5 % 10 =", f)  # Output: 5

g = 9 % 10
print("9 % 10 =", g)  # Output: 9

h = 10 % 10
print("10 % 10 =", h)  # Output: 0

# Exponential (**)
# Used to raise a number to the power of another
i = 5 ** 3
print("5 ** 3 =", i)  # Output: 125

# Floor Division (//)
# It gives the result in whole numbers (integer part only)
j = 10 // 4
print("10 // 4 =", j)  # Output: 2

k = -10 // 4
print("-10 // 4 =", k)  # Output: -3

# Assignment Operators - Make one example for each

x = 5
print("Initial x:", x)

x += 5    # x = x + 5
print("x += 5:", x)

x = 5
x -= 2    # x = x - 2
print("x -= 2:", x)

x = 5
x *= 3    # x = x * 3
print("x *= 3:", x)

x = 5
x /= 2    # x = x / 2
print("x /= 2:", x)

x = 5
x %= 3    # x = x % 3
print("x %= 3:", x)

x = 5
x //= 2   # x = x // 2
print("x //= 2:", x)

x = 5
x **= 2   # x = x ** 2
print("x **= 2:", x)



# Comparison Operators
# Comparison operators are used to compare two values.
# The result is always True or False.

# > Greater than
print("10 > 5 =", 10 > 5)  # True

# < Less than
print("4 < 9 =", 4 < 9)  # True

# >= Greater than or equal to
print("7 >= 7 =", 7 >= 7)  # True

# <= Less than or equal to
print("6 <= 3 =", 6 <= 3)  # False

# == Equal to
print("5 == 5 =", 5 == 5)  # True

# != Not equal to
print("8 != 10 =", 8 != 10)  # True

# Logical Operators
# Logical operators are used to combine multiple conditional statements.

x = 10
y = 20

# and -> returns True only if both conditions are True
print("x < 15 and y < 25:", x < 15 and y < 25)  # True

# or -> returns True if at least one condition is True
print("x > 15 or y > 15:", x > 15 or y > 15)  # True

# not -> reverses the result
print("not(x < 15 and y < 25):", not(x < 15 and y < 25))  # False

# Logic Gate Definitions

# AND Gate:
# - Returns True only when **both** inputs are True.
# - Truth Table:
#   A   B   A and B
#   0   0     0
#   0   1     0
#   1   0     0
#   1   1     1

# OR Gate:
# - Returns True when **at least one** input is True.
# - Truth Table:
#   A   B   A or B
#   0   0     0
#   0   1     1
#   1   0     1
#   1   1     1

# NOT Gate:
# - Reverses the input.
# - Truth Table:
#   A   not A
#   0     1
#   1     0

# NOR Gate:
# - Returns True only when **both** inputs are False (opposite of OR).
# - Truth Table:
#   A   B   A nor B
#   0   0     1
#   0   1     0
#   1   0     0
#   1   1     0



# Identity Operators
# Identity operators compare the memory locations of two objects 
# (i.e., whether they are the same object in memory).

# is       - Returns True if both refer to the same object     ---> x is y
# is not   - Returns True if they do not refer to the same object  ---> x is not y

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # Output: True  — same memory location
print(x is z)      # Output: False — different memory even if content is the same
print(x is not z)  # Output: True

# ---------------------------------------------

# Membership Operators
# Membership operators are used to check whether a value exists in a sequence 
# like a list, tuple, or string.

# in       - Returns True if value exists in the sequence      ---> 'a' in 'apple' -> True
# not in   - Returns True if value does not exist in sequence  ---> 'x' not in 'apple' -> True

print('a' in 'apple')     # Output: True
print('x' not in 'apple') # Output: True

# ---------------------------------------------

# Bitwise Operators
# Bitwise operators perform operations on binary (bit-level) representations of integers.

# Operator    Description          Example        Binary Operation
# &           Bitwise AND          5 & 3 = 1      0101 & 0011 = 0001
# |           Bitwise OR           5 | 3 = 7      0101 | 0011 = 0111
# ^           Bitwise XOR          5 ^ 3 = 6      0101 ^ 0011 = 0110
# ~           Bitwise NOT          ~5 = -6        ~0101 = -(0101 + 1)
# <<          Left Shift           5 << 1 = 10    0101 << 1 = 1010
# >>          Right Shift          5 >> 1 = 2     0101 >> 1 = 0010

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print(a & b)    # Output: 1  (AND)
print(a | b)    # Output: 7  (OR)
print(a ^ b)    # Output: 6  (XOR)
print(~a)       # Output: -6 (NOT)
print(a << 1)   # Output: 10 (Left shift by 1)
print(a >> 1)   # Output: 2  (Right shift by 1)