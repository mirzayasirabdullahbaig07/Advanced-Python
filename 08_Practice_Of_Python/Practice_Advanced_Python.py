# -------------------------------------------------------------
# Conceptual Python Questions and Answers with Explanations
# -------------------------------------------------------------

# -------------------------------
# File Paths and String Quotes
# -------------------------------

# Q1: Print the following path using escape sequences:
#     C:\Users\John\Desktop\File.txt
print("C:", "Users", "John", "Desktop", "File.txt", sep="\\")

# Q2: Print a message containing double quotes: He said, "Hello!".
msg = 'He said, "Hello!"'
print(msg)

# Q3: Print a message containing both single and double quotes:
#     She said, 'It's cold'.
msg2 = "She said, 'It's cold'."
print(msg2)

# -------------------------------
# Input, Output, and Conversion
# -------------------------------

# Q4: Add two numbers entered by the user.
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
result = num1 + num2
print(f"The sum of the two numbers is: {result}")

# Q5: Convert a string to an integer and vice versa.
str_num = "123"
print(int(str_num))  # String to integer

int_num = 123
print(str(int_num))  # Integer to string

# Q6: Calculate the area of a rectangle using user input.
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Q7: Calculate the average of three numbers entered by the user.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
average = (n1 + n2 + n3) / 3
print(f"The average is: {average}")

# Q8: Convert between float and integer.
float_val = 353.322
print(int(float_val))  # Float to int

int_val = 228392
print(float(int_val))  # Int to float

# Q9: Convert Fahrenheit to Celsius.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Temperature in Celsius: {celsius}")

# Q10: Calculate the total and percentage from 5 subjects.
marks = [23, 42, 53, 65, 32]
total = sum(marks)
percentage = (total / 500) * 100  # assuming each subject is out of 100
print("Total Marks =", total)
print("Percentage =", percentage)

# Q11: Tournament points calculator.
# 1 win = 4 points, 1 tie = 2 points
games = int(input("Enter the total number of games: "))
wins = int(input("Enter the number of wins: "))
losses = int(input("Enter the number of losses: "))
ties = games - (wins + losses)
points = (wins * 4) + (ties * 2)
print(f"Tied games: {ties}")
print(f"Total points: {points}")

# -------------------------------
# Arithmetic & Assignment Ops
# -------------------------------

# Q12: Perform arithmetic operations on two user-input numbers.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# Q13: Swap two variables without a temporary variable.
a = 2
b = 5
a, b = b, a
print("a =", a)
print("b =", b)

# Q14: Calculate compound interest.
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time (in years): "))
A = P * (1 + R / 100) ** T
print("Compound Interest Amount:", A)

# Q15: Calculate the area of a circle.
radius = float(input("Enter the radius: "))
area_circle = 3.14 * radius ** 2
print("Area of the circle =", area_circle)

# -------------------------------
# Comparison & Logical Ops
# -------------------------------

# Q16: Output of comparison
x = 5
y = 3
print(x > y)  # True

# Q17:
a = 10
b = 20
c = 30
print(a < b and b < c)  # True

# Q18:
p = True
q = False
print(not p or q)  # False

# Q19:
num1 = 15
num2 = 10
print(num1 == num2 or num1 > num2)  # True

# Q20:
m = 8
n = 6
print(m >= n and n != m)  # True

# Q21:
a = 5
b = 5
c = 10
print(a <= b and b != c)  # True

# Q22:
num = 25
print(num % 2 == 0)  # False → 25 is odd

# =====================================================
# If-Else Practice Questions (Q23 – Q26)
# =====================================================

# -----------------------------------------------------
# Q23. Check if a number is positive or negative
# (Note: Consider 0 as positive)
# -----------------------------------------------------
num = int(input("Enter an integer: "))

if num >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# -----------------------------------------------------
# Q24. Check if a character is a vowel or consonant
# (Use multiple OR conditions)
# -----------------------------------------------------
char = input("Enter a single character: ").lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# -----------------------------------------------------
# Q25. Check if the first number is divisible by the second
# -----------------------------------------------------
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
elif num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}.")
else:
    print(f"{num1} is not divisible by {num2}.")

# -----------------------------------------------------
# Q26. Check exam eligibility based on attendance
# Rule: Attendance must be at least 75%
# -----------------------------------------------------
classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print(" The student is allowed to sit in the exam.")
else:
    print(" The student is NOT allowed to sit in the exam.")

# IF - ELIF - ELSE
#Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero.
num = int(input("enter the number = "))

if num == 0:
    print("The number is zero.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q28. Write a program to check if number is divisible by 2 and 3 but not 8.
addNum = int(input("enter the number = "))

if addNum % 2 == 0 and addNum % 3 == 0 and addNum % 8 != 0:
    print("The number is divisible by 2 and 3 but NOT by 8.")
else:
    print("Condition not satisfied.")


# Q29. Write a program to print the last digit of a number. (NOT A IF ELSE
# QUESTION)
# Example 1
# Input: 45321
# Output: 1
# Example 2
# Input: 459094
# Output: 4

numinput = 13283429
num = numinput % 10
print(num)

# second method
a = numinput[-1]
print(a)


# Q30. Write a program to check if the last digit of a number is divisible by 5 or not.

num = 110030209221
num1 = num % 10
print(num1)

if num1 % 5 == 0:
    print("the num is divible by 5")
else:
    print("number is not divible by 5")
