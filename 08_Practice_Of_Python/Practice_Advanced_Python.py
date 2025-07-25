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

# Q31. Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.
# Example 1
# Enter bill amount = 80000
# You got 30% discount
# Your final bill is Rs. 56000

# Ask user for the final amount
amount = float(input("Enter bill amount: Rs. "))

# Apply discount based on amount
if amount >= 50000:
    discount = 30
elif amount >= 40000:
    discount = 25
elif amount >= 30000:
    discount = 20
elif amount >= 10000:
    discount = 10
elif amount >= 1:
    discount = 0
else:
    print("Invalid amount!")
    discount = None

# Calculate final bill and display result
if discount is not None:
    discount_amount = (discount / 100) * amount
    final_bill = amount - discount_amount
    print(f"You got {discount}% discount")
    print(f"Your final bill is Rs. {final_bill:.2f}")

# Q32. Ask 4 numbers from the user. Make sure all the numbers entered by user are different. Then print which number is the smallest.

print("Enter 4 different numbers:")

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))

# Check if all numbers are different
if len({a, b, c, d}) != 4:
    print("Error: All numbers must be different.")
else:
    smallest = min(a, b, c, d)
    print(f"The smallest number is: {smallest}")

# Q33 Ask a number from a user:
# print 'fizz' if number is divisble by 3.
# print 'bizz' if number is divisble by 5.
# print 'fizzbizz' if number is divisble by 3 and 5.
# print the number itself if none of the conditions are true.

number = int(input("enter the number = "))

if number % 3 == 0 and number % 5 == 0:
    print("fizzbizz")
elif number % 3 == 0 :
    print("fizz")
elif number % 5 == 0:
    print("bizz")
else:
    print(number)

# Q34. A student will not be allowed to sit in exam if his/her attendance is
# less than 75%.
# a. Take following input from user
# i. Number of classes held
# ii. Number of classes attended.
# b. Print percentage of class attended
# c. Print Is student is allowed to sit in exam or not.

# a. Take input from user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# b. Calculate percentage
attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

# c. Check eligibility
if attendance_percentage >= 75:
    print(" Student is allowed to sit in the exam.")
else:
    print(" Student is NOT allowed to sit in the exam.")

# Q35 Take three numbers as input from user and print which one is greater or they are equal
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print("Number 1 is greatest.")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is greatest.")
else:
    print("Number 3 is greatest.")

## Q36. T