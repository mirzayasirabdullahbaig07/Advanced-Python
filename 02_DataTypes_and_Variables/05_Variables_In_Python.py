#  Variables in Python

#  A variable is a **container** for storing data values.
#  Unlike some other languages (like Java or C++), **Python does not require declaring** a variable type before using it.
#  A variable is created as soon as you assign a value to it.

# Example: Assigning and printing variables
x = 5
print(x)  # Output: 5

y = "Yasir"
print(y)  # Output: Yasir

# You can perform operations using variables
a = 2
b = 4
c = a + b
print(c)  # Output: 6

name_var = "Mirza Yasir Abdullah Baig"
print(name_var)  # Output: Mirza Yasir Abdullah Baig

# ----------------------------------------------------------
# Rules to Name a Variable in Python
# ----------------------------------------------------------

# 1. Must start with a letter (a-z, A-Z) or an underscore (_)
# 2. Can only contain letters, numbers, and underscores (_)
#    →  No special characters (!, @, %, etc.)
#    →  No spaces
# 3. Variable names are **case-sensitive**
#    → myVar and myvar are different variables
# 4. Do NOT use Python keywords or built-in function names as variable names
#    → Examples to avoid: print, input, if, else, for, etc.
# 5. Use **descriptive names** that explain the purpose of the variable
#    → Examples: count, total_amount, user_name
# 6. Use **snake_case** for multiple words
#    → Example: user_name, item_price

# ----------------------------------------------------------
# Different Ways to Print Variables
# ----------------------------------------------------------

# Method 1: Using commas
name = "Yasir"
print("My name is", name)  # Output: My name is Yasir

# Method 2: Using f-strings (Recommended for formatting)
name_var = "Yasir"
print(f"My name is {name_var}")  # Output: My name is Yasir
