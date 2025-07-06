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
name = 'He said, "Hello!"'
print(name)

# Output: He said, "Hello!"


# Q3: Create a program that prints a message containing both single and
# double quotes, like this: She said, 'It's cold'.

# Solution:
# Use double quotes to wrap the string and single quotes inside, including an apostrophe in "It's".
name2 = "She said, 'It's cold'."
print(name2)

# Output: She said, 'It's cold'.



# Q4. Write a Python program to add two numbers entered by the user.
num1 = int(input("Enter the 1st number "))
num2 = int(input("Enter the 2nd number "))
result = num1 + num2
print(f"the sum of two numbers are {result}")


# Q5. Convert a string to an integer and vice versa.
str_int = "123"
print(int(str_int))

int_str = 123
print(str(int_str))


# Q6. Write a Python program to calculate the area of a rectangle using user
# input for length and width.



# Q7. Write a Python program to calculate the average of three numbers
# entered by the user.
# Q8. Convert a float to an integer and vice versa.
# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.
# Q10. Calculate sum of 5 subjects and Find percentage.
# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)


# ARITHMETIC & ASSIGNMENT
# Q12. Write a Python program that takes two numbers as input and
# performs the following operations: addition, subtraction, multiplication,
# division, and modulus. Display the results.
# Q13. Write a Python program to swap the values of two variables without
# using a temporary variable.
# Q14. Write a Python program to calculate the compound interest for a
# given principal, rate of interest, and time period. Ask everything from the
# user.
# Q15. Write a Python program that takes the radius of a circle as input and
# calculates its area. Use the formula: Area = 3.14 * r^2.


