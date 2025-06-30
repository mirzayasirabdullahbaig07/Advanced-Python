# Conditional Statements
# Conditional statements (if, else, and elif) allow us to control the flow of the program.
# They help make decisions based on conditions.

# Types of Conditional Statements:
# 1. if statement
# 2. else statement
# 3. elif (else if) statement
# 4. nested if-else

# Example 1: Check if a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
    print("You are allowed to vote")
else:
    print("You cannot vote")

# Example 2: Check which number is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Number 1 is greater")
else:
    print("Number 2 is greater")

# Example 3: Check if the number is odd or even
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Multiple Conditions using if-elif-else
# Syntax:
# if condition:
#     ---
# elif condition:
#     ---
# elif condition:
#     ---
# else:
#     ---

# Example: Compare two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Number 1 is greater")
elif num1 < num2:
    print("Number 2 is greater")
else:
    print("Both numbers are equal")

# Example: Grading system based on marks in 5 subjects
marks = int(input("Enter your average marks (0-100): "))

if marks >= 91 and marks <= 100:
    print("Grade: A")
elif marks >= 81 and marks <= 90:
    print("Grade: B")
elif marks >= 71 and marks <= 80:
    print("Grade: C")
elif marks >= 61 and marks <= 70:
    print("Grade: D")
elif marks >= 0 and marks <= 60:
    print("Fail")
else:
    print("Invalid Marks")

# Nested if-else statement
# Example: Check if a number is positive and even or odd

number = int(input("Enter a number: "))

if number >= 0:
    print("Number is positive")
    
    if number % 2 == 0:
        print("It's even")
    else:
        print("It's odd")
else:
    print("Number is negative")
