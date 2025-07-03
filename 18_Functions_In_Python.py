# -------------------------------------------
# Functions in Python - Complete Guide
# -------------------------------------------

# Why Use Functions in Python?
# Functions help:
# - Organize code into blocks
# - Avoid repetition (DRY Principle: Don’t Repeat Yourself)
# - Make code modular, reusable, and readable
# - Perform specific tasks independently

# -------------------------------------------
# Syntax of a Function
# -------------------------------------------

# def function_name(parameters):
#     """docstring (optional)"""
#     # function body
#     return value (optional)

# -------------------------------------------
# Example: A simple function
def greet():
    """This function prints a greeting message"""
    print("Hello, welcome to Python functions!")

greet()  # Calling the function

# -------------------------------------------
# Return vs Print
# -------------------------------------------

# - print(): displays output to the console
# - return: sends data back to the caller for further use

def add(x, y):
    return x + y  # returns the result to the caller

result = add(5, 3)
print("Returned value:", result)

# -------------------------------------------
# Parameters vs Arguments
# -------------------------------------------

# Parameters: variables inside function definition
# Arguments: actual values passed when calling the function

def say_hello(name):  # name = parameter
    print("Hello", name)

say_hello("Yasir")  # "Yasir" = argument

# -------------------------------------------
# Types of Parameters
# 1. Required Parameters
# 2. Default Parameters
# 3. Keyword (Named) Parameters
# 4. Variable-length Parameters (*args, **kwargs)

# 1. Required Parameter
def required_example(name):
    print("Name is", name)

required_example("Ali")

# 2. Default Parameter
def default_example(city="Lahore"):
    print("City is", city)

default_example()         # uses default
default_example("Karachi")  # overrides default

# 3. Named (Keyword) Parameter
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=21, name="Sana")  # order doesn't matter

# 4. Variable-length Parameters
def many_args(*args):  # collects values into a tuple
    print("Args:", args)

many_args(1, 2, 3, "Python")

def many_kwargs(**kwargs):  # collects named values into a dict
    print("Kwargs:", kwargs)

many_kwargs(name="Sara", age=22)

# -------------------------------------------
# Scope in Functions
# -------------------------------------------

# - Local Scope: Variables declared inside a function
# - Global Scope: Variables declared outside all functions

# Local Scope
def local_scope():
    a = 10  # local variable
    print("Inside function:", a)

local_scope()
# print(a)  # Error: 'a' is not defined outside

# Global Scope
b = 20  # global variable

def global_scope():
    print("Inside function, global b:", b)

global_scope()
print("Outside function, global b:", b)

# Using global keyword
x = 5

def modify_global():
    global x
    x = 10

modify_global()
print("Modified global x:", x)

# -------------------------------------------
# Function with No Return
def just_print():
    print("This function does not return anything")

# Function with Return
def square(n):
    return n * n

print(square(4))

# -------------------------------------------
#   Summary
# - def = keyword to define a function
# - Functions can return values or simply perform tasks
# - Parameters and arguments help customize function behavior
# - Scope determines variable visibility
# - Use global keyword to modify global variables
# - *args and **kwargs support flexible argument passing
