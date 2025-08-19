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

# Q36 Take Salary as input from User and Update the salary of an employee.
# salary less than 10,000, 5 % increment
# salary between 10,000 and 20, 000, 10 % increment
# salary between 20,000 and 50,000, 15 % increment
# salary more than 50,000, 20 % increment
input_salary = int(input("Enter the current salary: "))

if input_salary < 10000: # less than 10000
    increment = 0.05 * input_salary
elif 10000 <= input_salary <= 20000:
    increment = 0.10 * input_salary
elif 20001 <= input_salary <= 50000:
    increment = 0.15 * input_salary
else:
    increment = 0.20 * input_salary

updated_salary = input_salary + increment
print(f"Increment: {increment}")
print(f"Updated Salary: {updated_salary}")
# must do it again

# Q37: An extra day is added to the calendar almost every four years as
# February 29, and the day is called a leap day. A leap year contains a leap
# day.


# These are the conditions used to identify leap years:

# if the year can be evenly divided by 4, it is then a leap year
# but if the year is evenly divided by 4 and also by 100, then it is NOT a
# leap year
# but if the year is evenly divided by 4 and also by 400, then it is a leap
# year
# This means the years 2000 and 2400 are leap years, while 1800, 1900,
# 2100, 2200, 2300 and 2500 are NOT leap years.
# Ask a year input from user. And tell if the year entered by user is leap or
# not

input_Year = int(input("Enter the year: "))

if input_Year % 4 == 0:
    if input_Year % 100 == 0:
        if input_Year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")

#   question 38 to 41 nested if else statements

# Q38. Write a program that takes three numbers as input and determines
# the largest one using nested if-else statements. Make sure all 3 numbers
# entered by user are dierent
# Q38. Write a program that takes three numbers as input and determines
# the largest one using nested if-else statements. Make sure all 3 numbers
# entered by user are different

input_1 = int(input("enter the first number = "))
input_2 = int(input("enter the second number = "))
input_3 = int(input("enter the third number = "))

# Check if all numbers are different
if input_1 != input_2 and input_1 != input_3 and input_2 != input_3:
    if input_1 > input_2:
        if input_1 > input_3:
            print("First number is the greatest.")
        else:
            print("Third number is the greatest.")
    else:
        if input_2 > input_3:
            print("Second number is the greatest.")
        else:
            print("Third number is the greatest.")
else:
    print("Please enter three different numbers. They must be unique.")

# Q39. Write a program that checks if a given year is a leap year. Leap years
# are divisible by 4, but not by 100 unless they are also divisible by 400.
enter_year = int(input("enter the year = "))

if enter_year % 4 == 0:
    if enter_year % 100 == 0:
        if enter_year % 400 == 0:
            print("It is a leap year")  # divisible by 400
        else:
            print("It is not a leap year")  # divisible by 100 but not 400
    else:
        print("It is a leap year")  # divisible by 4 but not by 100
else:
    print("It is not a leap year")  # not divisible by 4

# Q40. Create a program that calculates the price of a movie ticket based on the age of the customer. If the customer is under 12, the ticket costs $5; if they are between 12 and 65, the ticket costs $10; otherwise, it's $7.
movie_ticket = int(input("age of a customer = "))
if movie_ticket > 12:
    print("the price is 5")
else:
    if movie_ticket <= 65:
        print("it is 10")
    else:
        print("it is 7")

# Q41. Write a program that calculates a person's BMI based on their height
# (in meters) and weight (in kilograms). Use the following formula: BMI =
# weight / (height^2). Then, classify the BMI according to the following
# ranges:
# Underweight: BMI less than 18.5
# Normal weight: BMI 18.5 - 24.9
# Overweight: BMI 25 - 29.9
# Obesity: BMI 30 or greater
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight.")
else:
    if bmi < 25:
        print("You have a normal weight.")
    else:
        if bmi < 30:
            print("You are overweight.")
        else:
            print("You are obese.")

# BASIC WHILE LOOP
# Q42. Ask a number from user. Print all the numbers from 1 to that number.
user_do = int(input("enter the number = "))
i = 1
while i <= user_do:
    print(i)
    i  = i + 1
    
# Q43. Ask a number (N) from user. Print all the numbers from N to 1.
user_do = int(input("enter the number = "))
i = user_do
while i >= 1:
    print(i)
    i = i - 1
# Q44. Ask start number and end number from user. Print all the numbers
# from start to end using while loop.
start = int(input("enter the first number "))
end = int(input("enter the last number "))
i = start
while i <= end:
    print(i)
    i = i + 1
# Q45. Calculate the sum of all the numbers from 1 to 10.
i = 1
total = 0

while i <= 10:
    total = total + i
    i = i + 1
print(f"sum is {total}")
# Q46. Calculate product of all the numbers from 1 to 10.

i = 1
total = 1

while i <= 10:
    total = total * i
    i = i + 1
print(f"the total product is {total}")
# Q47. Calculate how many numbers are divisible by 7 from 1 to 100.
i = 1
count = 0
while i <= 100:
    if i % 7 == 0:
       count = count + 1
    i = i + 1
print(f"the value is {count}")
# Q48. Calculate how many numbers are divisible by both 6 and 7 between 1
# to 200.
i = 1
count = 0

while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    i = i + 1
print(f"the total count is {count}")
# Q49. Write a program to calculate the sum of all the numbers divisible by 4
# from 20 to 50.
num = 0
i = 20
while i <= 50:
    if i % 4 == 0:
        num = num + i
    i = i + 1
print(f"the sum is {num}")


# Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to
# 200.
i = 1
count = 0

while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    i = i + 1
print(f"the count is {count}")

# Q51. Ask a number from user. Print the multiplication table of that number.
# Example
# Enter a number = 8
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 10 = 80

enter_ = int(input("enter the number = "))
i = 1

table = 1

while i <= 10:
    table = enter_ * i 
    print(f"the table is {enter_} *{ i }= {table}")
    i = i + 1
    


# Q52. Calculate factorial of a number entered by user.
# Example:
# Enter a number = 5
# Factorial of a number means product of all the numbers from 1 to that
# number.
# 5 factorial = 5 x 4 x 3 x 2 x 1
# Output = 120

number = int(input("enter the number = "))

i = 1
factorial = 1

while i <= number:
    factorial = factorial * i
    i = i + 1

print(f"the factorial is {factorial}")



# Q53. Ask to numbers x and y from the user. If x<y then print all the
# numbers from x to y, but if y<x then print all the numbers from y to x.

# Q53: Print all numbers from x to y if x < y, otherwise from y to x

x = int(input("Enter the number x = "))
y = int(input("Enter the number y = "))

if x < y:
    i = x
    while i <= y:
        print(i)
        i += 1
else:
    i = y
    while i <= x:
        print(i)
        i += 1



# BASIC FOR LOOP
# Q54. Ask a number from user. Print all the numbers from 1 to that number.
add_ = int(input("enter the number = "))

for i in range(1, add_ + 1):
    print(i)


# Q55. Ask a number (N) from user. Print all the numbers from N to 1.
num_ = int(input("enter the number = "))

for i in range(num_, 0, - 1):
    print(i)
# Q56. Ask start number and end number from user. Print all the numbers from start to end using while loop.
start = int(input("enter the first number "))
end = int(input("enter the last number "))

for i in range(start, end + 1):
    print(i)
# Q57. Calculate the sum of all the numbers from 1 to 10.

count = 0
for i in range(1, 10):
    count = count + 1
print(count)
# Q58. Calculate product of all the numbers from 1 to 10.

count = 1
for i in range(1, 11):
    count = count * i
print(f"the count is {count}")
# Q59. Calculate how many numbers are divisible by 7 from 1 to 100.
count = 0

for i in range(1, 101):
    if i % 7 == 0:
        count = count + 1
print(f"count is {count}")
# Q60. Calculate how many numbers are divisible by both 6 and 7 between 1
# to 200

count = 0

for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    print(f"count is {count}")


# Q 63 Ask a number from user. Print the multiplication table of that number.
# Example
# Enter a number = 8
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
table_ = int(input("enter the number = "))

for i in range(1, 11):
    table1_ = table_ * i
    print(f"{table_} * {i} = {table1_}")



# Q64. Calculate factorial of a number entered by user.
# Example:
# Enter a number = 5
# Factorial of a number means product of all the numbers from 1 to that
# number.
# 5 factorial = 5 x 4 x 3 x 2 x 1
# Output = 120

num = int(input("enter the number = "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"the value of the factorial is = {factorial}")


# Q65. Ask to numbers x and y from the user. If x<y then print all the
# numbers from x to y, but if y<x then print all the numbers from y to x.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x < y:
    for i in range(x, y + 1):
        print(i)
else:
    for i in range(y, x + 1):
        print(i)

# NESTED LOOPS question patterns with explanations

# Q66: Create a pattern using nested loop
# *****
# *****
# *****
# *****
# *****
for i in range(5):                         # Outer loop for 5 rows
    for j in range(5):                     # Inner loop for 5 columns
        print("*", end="")                 # Print star without newline
    print()                                # Move to next line after each row

print("\n" + "-"*20)

# Q67: Create a pattern using nested loop
# 12345
# 12345
# 12345
# 12345
# 12345
for i in range(5):                         # Outer loop for rows
    for j in range(1, 6):                  # Print numbers from 1 to 5
        print(j, end="")
    print()

print("\n" + "-"*20)

# Q68: Create a pattern using nested loop
# 54321
# 54321
# 54321
# 54321
# 54321
for i in range(5):                         # Outer loop for rows
    for j in range(5, 0, -1):              # Print numbers from 5 to 1
        print(j, end="")
    print()

print("\n" + "-"*20)

# Q69: Create a pattern using nested loop
# 11111
# 22222
# 33333
# 44444
# 55555
for i in range(1, 6):                      # Rows from 1 to 5
    for j in range(5):                     # 5 columns each
        print(i, end="")                   # Print same number in each row
    print()

print("\n" + "-"*20)

# Q70: Create a pattern using nested loop
# 55555
# 44444
# 33333
# 22222
# 11111
for i in range(5, 0, -1):                  # Rows from 5 down to 1
    for j in range(5):                     # 5 columns each
        print(i, end="")
    print()

print("\n" + "-"*20)

# Q71: Ask N from user. Print pattern:
# Example N=6
# 111111
# 222222
# 333333
# 444444
# 555555
# 666666
n = int(input("Enter the number of lines (Q71): "))
for i in range(1, n + 1):                  # Rows from 1 to n
    for j in range(n):                     # Columns: print i, n times
        print(i, end="")
    print()

print("\n" + "-"*20)

# Q72: Ask N from user. Print pattern:
# Example N=9
# 888888888
# 777777777
# 666666666
# 555555555
# 444444444
# 333333333
# 222222222
# 111111111
# 000000000
n = int(input("Enter the number of lines (Q72): "))
for i in range(n - 1, -1, -1):             # Rows from n-1 to 0
    for j in range(n):                     # Columns: print i
        print(i, end="")
    print()

# Q73: Print the following pattern.
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):              # Print from 1 to i
        print(j, end="")
    print()

# Q74: Print the following pattern.
# 1
# 22
# 333
# 4444
# 55555
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

# Q75: Print the following pattern.
# 1
# 21
# 321
# 4321
# 54321
for i in range(1, 6):
    for j in range(i, 0, -1):              # Print from i down to 1
        print(j, end="")
    print()

# Q76: Print the following pattern.
# 5
# 54
# 543
# 5432
# 54321
for i in range(1, 6):
    for j in range(5, 5 - i, -1):          # Start at 5, go down i times
        print(j, end="")
    print()

# Q77: Print the following pattern.
# 5
# 44
# 333
# 2222
# 11111
for i in range(1, 6):
    for j in range(i):
        print(6 - i, end="")               # Print decreasing number each row
    print()

# Q78: Print the following pattern.
# *
# **
# ***
# ****
# *****
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Q79: Print the following pattern.
# 54321
# 5432
# 543
# 54
# 5
for i in range(5, 0, -1):
    for j in range(i):
        print(5 - j, end="")               # Count forward within each row
    print()

# Q80: Print the following pattern.
# 55555
# 4444
# 333
# 22
# 1
for i in range(5, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

# Q81: Print the following pattern.
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Q82: Print the following pattern.
# 54321
# 4321
# 321
# 21
# 1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Q83: Print the following pattern.
# 1
# 23
# 456
# 78910
# 1112131415
count = 1
for i in range(1, 6):
    for j in range(i):
        print(count, end="")
        count += 1
    print()

# Q84: Same as Q83 — continue increasing numbers in triangle
count = 1
for i in range(1, 6):
    for j in range(i):
        print(count, end="")
        count += 1
    print()

# Q85: Print the following pattern.
#     *
#    **
#   ***
#  ****
# *****
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q86: Print the following pattern.
#     1
#    22
#   333
#  4444
# 55555
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

# Q87: Print the following pattern.
#     1
#    12
#   123
#  1234
# 12345
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(k + 1, end="")
    print()

# Q88: Print the following pattern.
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q89: Print the following diamond pattern.
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q90: Print the following inverted pyramid.
# *********
#  *******
#   *****
#    ***
#     *
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q91: Print inverted + upright pyramid.
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(2, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# BASIC LIST ITERATION
# Q92. Make your own list. Print the list in reverse

list_ = ["yasir", 7, "Yasir Insights", False, 0.7]

print(list_[::-1])

# Q93. Make your own list. Print all the even numbers present in the list
list_ = [1,2,3,4,5,6,7,8,9,10]
for var in list_:
    if var % 2 == 0:
        print(var, end = " ")

# Q94. Make your own list. Print all the odd numbers present in the list

list_ = [1,2,3,4,5,6,7,8,9,10]
for var in list_:
    if var % 3 == 0:
        print(var, end = " ")

# Q95. Make your own list. Print all the elements present at even index position.
list_ = ["yasir", 7, "Yasir Insights", False, 0.7]
print(list_[0::2])


# Q96. Make your own list. Print the sum of all elements present in that list.
list_ = [1,2,3,4,5,6,7,8,9,10]
print(sum(list_))

# Q97. Make your own list. Count the number of even numbers present in
# that list
list_ = [1,2,3,4,5,6,7,8,9,10]
even = 0
for a in list_:
    if a % 2 == 0:
        even = even + 1
print(even)


#Q98. Make your own list. Count how many numbers are divisible by both 2
# and 5 in that list. (Do on your own)

list_ = [1,2,3,45,5,6,6,6,7,7,8,9,0,10,4,55,754,25,50, 60]
count = 0
for i in list_:
    if i % 2 == 0 and i % 5 == 0:
        count = count + 1
print(count)


# 99 Make your own list. Find the sum of all even numbers present in that

list_ = [1,2,3,45,5,6,6,6,7,7,8,9,0,10,4,55,754,25,50, 60]
even = 0
for a in list_:
    if a % 2 ==0:
        
        even += a
print(even)

# Q100. Make your own list. Find the sum of all numbers divisible by 3 or 4.
# (Do on your own)

list_ = [1,2,3,45,5,6,6,6,7,7,8,9,0,10,4,55,754,25,50, 60]
sum_ = 0

for i in list_:
    if i % 3 == 0 or i % 4 == 0:
        sum_ = sum_ + i
print(sum_)

# Q101: Make your own list. Print how many positive and negative numbers are here. (Do on your own)
list_ = [1,2,4,5,6,6,-67,4,-6,-4,-44,3,-3,2]
postive_ = 0 
neg_ = 0

for i in list_:
    if i > 0:
        postive_ = postive_ + 1
    if i < 0:
        neg_ = neg_ + 1
print(postive_)
print(neg_)


# Q 102 Make your own list. Print the largest number present in that list.
list_ = [1,2,4,5,6,67,4,-6,-4,-44,3,-3,2]
largeest = list_[0]
for i in list_:
    if i > largeest:
        largeest = i
print(largeest) 

# Q 103 Make your own list. Print the largest number present in that list.

list_ = [1,2,4,5,6,67,4,-6,-4,-44,3,-3,2]
largeest = list_[0]
for i in list_:
    if i < largeest:
        largeest = i
print(largeest)


# LIST METHODS (BASIC)
# #Q104. Write a program that prompts the user to specify the length o a list and then requests numbers to populate that list. Display the final list as the output.


value = int(input("enter how many numbers you want in the list = "))
answer = []
for i in range(value):
    num = int(input(f"enter the number {i + 1}"))
    answer.append(num)

print(answer)

# Q105. Create a list and prompt the user for an 'old number' followed by a
# 'new number.' If the 'old number' exists in the list, replace it with the 'new
# number' provided by the user.

# Step 1: Create the list
list_ = [1,2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,17]

num_odd = int(input("Enter the old number = "))
if num_odd % 2 != 0:
    print(f"{num_odd} is odd")
else:
    print(f"{num_odd} is not odd")

if num_odd in list_:
    new_num = int(input("Enter the new number = "))
    index = list_.index(num_odd)  
    list_[index] = new_num        
else:
    print("Number not found in the list.")

print(list_)


# Q 106 Remove all the even numbers from the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
numbers = odd_numbers
print(numbers)

# an other solution

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [num for num in numbers if num % 2 != 0]
print(number)

# Q107. Ask the user for a number. Then, from a list of numbers, 
# remove all the numbers that can be divided by the number the user entered.

# Original list
list__ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15]

# Empty list to store the remaining numbers
list_ = []

# Ask user for a number
num = int(input("Enter the number: "))

# Loop through each element in the original list
for i in list__:
    # If i is NOT divisible by num, keep it
    if i % num != 0:
        list_.append(i)  # Add to the new list

# Print the filtered list
print("Filtered list:", list_)
 


# 108. Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even.' Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.

list_ = [1,2,3,4,5,6,7,8,9,10]

odd_ = []
even_ = []

for i in list_:
    if i % 2 == 0:
        even_.append(i)
    else:
        odd_.append(i)
print(odd_)
print(even_)

# q 109 Start by creating two separate lists with random numbers. Then, create a third list that merges the numbers from the first and second lists together.
list_ = [1, 2, 3, 3, 4, 5, 5, 5]
list__ = [2, 43, 5, 5, 3, 5, 2, 1, 10]

# Merge both lists
list_new = list_ + list__

print(list_new)


# 110. Make a list of your own. And remove all the duplicates element from
# that list.

list_ = [1,1,1,1,1,3,3,3,2,3,4,5,7,8,6,9,0,10]
list__ = []

for i in list_:
    if i not in list__:
        list__.append(i)
print(list__)

# Q111. Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.
list_ = [1,2,3,4,5,56,7,8,9,9,0,2,3,4,5,68,7]
num = int(input("enter the value = "))


if num in list_:
    position = list_.index(num)
    print(position)
else:
    print(-1)

# Q112. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
list_ = []

for i in range(10):
    num = int(input("enter the number = "))
    list_.append(num)
list__ = list_[::-1]

print(list_)
print(list__)

#Q113. Write a program to find the average of all the numbers present in the list. (Do on your own)

list_ = [1,2,3,5,6,7,8,9,0,8,6,5,4,6]
for i in list_:
    list__ = (i / len(list_) ) * 100
print(list__)

# Q114: Find the occurrence of each element and print the one with highest occurrence

list_ = [1, 2, 3, 4, 5, 5, 5, 5, 8, 6, 6, 4, 2, 4, 6]
# Step 1: Count occurrences using a dictionary
occurrences = {}
for num in list_:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1
# Step 2: Find the element with the highest occurrence
max_element = max(occurrences, key=occurrences.get)
max_count = occurrences[max_element]
# Step 3: Print result
print("Occurrences:", occurrences)
print(f"Element with highest occurrence: {max_element} (appears {max_count} times)")


 # Q115. Write a program that has two lists and make a new list that contains only the common elements between them without duplicates

a = [1,2,3,4,4,5,56,6,7,7]
b = [1,4,56,7,8,8]
c = []

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)


# Q117. Make a program that takes a list of integers and returns the product of all the elements

list_ = [1,2,3,4,4,5,5,65,6]

for i in list_:
    list_ = list_ * i

print(list_)

list_ = [1,3,4,5,6,7,78,88,74]

largest = second_largest = float('-inf')

for num in list_:
    if num > largest:
        second_largest = largest 
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)



# 117. Make a program that takes a list of integers and returns the product of all the elements.
list_ = [1,2,3,4,4,5,5,65,6]
list__ = 1
for i in list_:
    list__ = list__ * i

print(list__)

#Q 118  Write a program to find and print all prime numbers within a given list
list_ = [1,2,3,3,4,45,5,6,6,7,87,8,8]
list__ = []
for i in list_:
    
    if i % 2 != 0:
        list__.append(i)
print(list_new)

# Q119. Write a program to split a given list into two halves. (Do on your own)
list_ = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

mid = len(list_) // 2  # Find midpoint

list_a = list_[:mid]  # First half
list_b = list_[mid:]  # Second half

print(list_a)
print(list_b)


#Q120. Write a program that swaps the first and last elements of a given list.

list_ = [1,2,3,4,5,56,6,7,8,9]

list_[0], list_[-1] = list_[-1], list_[0]

print(list_)



# Q121. Generate a list of squares of numbers from 1 to 10 using list comprehension

square_ = [x**2 for x in range(1, 11)]
print(square_)

# Q122. Given a list of strings, create a new list containing the lengths of each string using list comprehension
my_list = ["mirza", "yasir", "abdullah", "baig"]

sample_list = [len(i) for i in my_list]
print(sample_list)


#Q123. Generate a list of strings where each string repeats itself three times, using list comprehension.
my_list = ["mirza", "yasir", "abdullah", "baig"]
sample_list = [i*3 for i in my_list]
print(sample_list)


# Q124. Generate a list of list using list comprehension where format should be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]].
my_list = [1,1,3,4,5,6,67,7,8,9,9,8]
sample_list = [[i, "ODD"] if i % 2 != 0 else [i, "EVEN"] for i in my_list]
print(sample_list)


# List Slicing Questions Practice
# Q125. Write a python program to reverse a list using slicing.
list_ = [1,1,3,4,5,6,67,7,8,9,9,8]
print(list_[::-1])


# Q126. Write a python program to get every third element from a list using slicing.

my_list = ["mirza", "yasir", "abdullah", "baig", "mirza", "yasir", "abdullah", "baig"]
print(my_list[::3])

# Q127. Implement a python program to split a list into two equal parts using
# slicing. One list should contain 1st half and another list should contain 2nd
# half
my_list = ["1", "2", "2", "4", "mirza", "yasir", "abdullah", "baig"]
mid = len(my_list) // 2

list_a = my_list[:mid]
list_b = my_list[mid:]

print(list_a)
print(list_b)


# Q128. Implement a python program to get the last 'n' elements from a list using slicing.

a = [1, 2, 3, 4, 5, 6, 6, 7, 78, 8, 9, 9, 0]
n = int(input("Enter the nth value = "))

last_n_elements = a[-n:]
print(last_n_elements)

# Q129. Ask ‘n’ from user. Create a list of last n elements but in reverse order using slicing.
a = [1, 2, 3, 4, 5, 6, 6, 7, 78, 8, 9, 9, 0]
n = int(input("Enter the nth value = "))

last_n_elements = a[-n:][::-1]
print(last_n_elements)

#Q130. Ask start and end index from the user. Create a list from start index to end index using slicing.
a = [1, 2, 3, 4, 5, 6, 6, 7, 78, 8, 9, 9, 0]
start = int(input("enter the value - "))
end = int(input("enter the value - "))

sub_list = a[start:end]
print(sub_list)

# Q131. Ask start and end index from the user. Create a list of last n elements but in reverse order using slicing.
a = [1, 2, 3, 4, 5, 6, 6, 7, 78, 8, 9, 9, 0]
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

reversed_slice = a[start:end][::-1]
print(reversed_slice)


# STRING METHODS - 1
# Q132. Ask a string from user. Count how many alphabets are there in that
# string

str_ = "YasirAbdullahBaig"

count = 0

for ch in str_:
    if ch.isalpha():
        count = count + 1
print(count)

# Q133. Ask a string from user. Count the number of uppercase an lowercase characters in that String.
str_ = "YasirAbdullahBaig"
upper_count = 0
lower_count = 0

for ch in str_:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

# Q134. Ask a string from user. Convert all the alphabets to uppercase.
str_ = "YasirAbdullahBaig"
str_upper = str_.upper()

print(str_upper)


# Q135. Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and don’t change the other letters. (Do on your own)

text = input("enter the string: ")

result = " "


for char in text:
    if char.isupper:
        result = result + char.lower() 
    elif char.islower:
        result = result + char.upper()
    else:
        result = result + char


print(result)

# Q136. Count the number of spaces in a string entered by user.
str_ = "yasir            abdullah"

print(str_.count(" "))

# Q137. Ask a string from user. Print the count of how many alphabets, digits, spaces and symbols (everything else) are there in that string. (Do on your own)
text = input("enter the string: ")

alphabets = 0
digits = 0
spaces = 0
symbols = 0

for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        space += 1
    else:
        symbols += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Symbols:", symbols)


# STRING METHODS - 2


# Q138. Write a program to reverse the order of words.

str_ = "yasir abdullah"
reversed_str = " ".join(str_.split()[::-1])
print(reversed_str)


# Q139. Write a program that accepts a string and capitalizes the first letter of each word while converting all other letters to lowercase.

str_ = input("Enter a string: ")

# Capitalize first letter of each word & make others lowercase
result = str_.title()

print("Formatted string:", result)


# Q140. Write a program that reverses each word in a sentence while maintaining the word order. For example, "Hello World" should become "olleH dlroW".
str_ = "yasir abdullah"
reversed_words = " ".join(word[::-1] for word in str_.split())
print(reversed_words)

# Q141. Write a program that converts a string in camelCase to snake_case. For example, converting "helloWorldHowAreYou" should result in "hello_world_how_are_you". (Do on your own)

def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():  # If character is uppercase
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str

# Example usage
camel_string = "helloWorldHowAreYou"
snake_string = camel_to_snake(camel_string)
print(snake_string)



# Dictionary iteration
# Q142- Ask subject name and marks from the user and keep adding it to the dictionary?
 
#Ask total number of subjects
subject_count = int(input("Enter the total number of subjects: "))

# Create an empty dictionary
subjects = {}

# Loop to take input for each subject
for i in range(subject_count):
    sub = input(f"Enter the name of subject {i+1}: ")
    marks = int(input(f"Enter the marks for {sub}: "))
    subjects[sub] = marks  # store subject and marks in dictionary

# Print final dictionary
print("\nSubjects and Marks:")
print(subjects)

# Q143. Convert two lists into a dictionary. Make two list on your own of
# same length, and convert them to dictionary.
list_ = ['ten', 'twenty', 'thirty']
list__ = [10, 20, 30]

dic_ = {}

for i in range(len(list_)):
    dic_[list_[i]] = list__[i]   # assign key-value pair

print(dic_)



# Q144. Write a Python program to sum all the items in a dictionary.
# Dictionary with key-value pairs
dic_ = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Method 1: Using loop
total = 0
for value in dic_.values():
    total += value

print("Sum of all items:", total)

# Method 2: Using sum() directly
print("Sum of all items (using sum):", sum(dic_.values()))



# Q145: Write a Python program to multiply all the items in a dictionary. (Do on your own)
dic_ = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
total = 1
for i in dic_.values():
    total *= i
print(total)
