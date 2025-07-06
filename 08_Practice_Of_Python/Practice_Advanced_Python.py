# ---------------------------------------------
# Conceptual Questions and Answers with Logic
# ---------------------------------------------

# Q1: Write a program that prints a path like this:
# C:\Users\John\Desktop\File.txt using the appropriate escape sequences.

# Solution:
# We use the 'sep' parameter in print() to insert backslashes between each part.
print("C:", "Users", "John", "Desktop", "File.txt", sep="\\")

# Output: C:\Users\John\Desktop\File.txt


# Q2: Write a Python program that prints a message with a double-quote
# character inside it. Example: He said, "Hello!".

# Solution:
# Use single quotes to wrap the string, allowing double quotes inside without escaping.
msg = 'He said, "Hello!"'
print(msg)

# Output: He said, "Hello!"


# Q3: Create a program that prints a message containing both single and
# double quotes, like this: She said, 'It's cold'.

# Solution:
# Use double quotes to wrap the string and single quotes inside, including an apostrophe in "It's".
msg2 = "She said, 'It's cold'."
print(msg2)

# Output: She said, 'It's cold'.


# Q4. Write a Python program to add two numbers entered by the user.
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
result = num1 + num2
print(f"The sum of two numbers is {result}")


# Q5. Convert a string to an integer and vice versa.
str_num = "123"
print(int(str_num))  # string to int

int_num = 123
print(str(int_num))  # int to string


# Q6. Write a Python program to calculate the area of a rectangle using user input for length and width.
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is {area}")


# Q7. Write a Python program to calculate the average of three numbers entered by the user.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
average = (n1 + n2 + n3) / 3
print(f"The average of the numbers is {average}")


# Q8. Convert a float to an integer and vice versa.
float_val = 353.322
print(int(float_val))  # float to int

int_val = 228392
print(float(int_val))  # int to float


# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.
fahrenheit = 30
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)


# Q10. Calculate sum of 5 subjects and Find percentage.
marks = [23, 42, 53, 65, 32]
total = sum(marks)
percentage = (total / (5 * 100)) * 100  # assuming each subject is out of 100
print("Total Marks =", total)
print("Percentage =", percentage)


# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games lost. Calculate number of tie and total
# points. (1 win = 4 points, 1 tie = 2 points)
games = int(input("Enter the total number of games: "))
wins = int(input("Enter number of wins: "))
losses = int(input("Enter number of losses: "))
ties = games - (wins + losses)
points = (wins * 4) + (ties * 2)
print(f"Number of tie games = {ties}")
print(f"Total points = {points}")


# ARITHMETIC & ASSIGNMENT
# Q12. Write a Python program that takes two numbers as input and
# performs the following operations: addition, subtraction, multiplication,
# division, and modulus. Display the results.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)


# Q13. Write a Python program to swap the values of two variables without using a temporary variable.
a = 2
b = 5
a, b = b, a
print("a =", a)
print("b =", b)


# Q14. Write a Python program to calculate the compound interest for a
# given principal, rate of interest, and time period. Ask everything from the user.
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time (in years): "))
A = P * (1 + R / 100) ** T
print("Compound Interest Amount:", A)


# Q15. Write a Python program that takes the radius of a circle as input and calculates its area.
# Use the formula: Area = 3.14 * r^2.
radius = float(input("Enter the radius: "))
area_circle = 3.14 * radius ** 2
print("Area of the circle =", area_circle)
