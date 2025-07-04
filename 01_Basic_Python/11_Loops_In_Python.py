# What are Loops?
# Looping means repeating a block of code multiple times until a particular condition is satisfied.

# Main types of loops in Python:
# 1. while loop
# 2. for loop

# -------------------------------
# while loop
# Syntax:
# while condition:
#     code
#     code
# It will keep executing the block as long as the condition is True.

print("This will print after the while loop ends (when the condition becomes False)")

# Example: Print "Hello world" multiple times

# Infinite loop (Don't run this)
# i = 1
# while i < 10:
#     print("Hello world")

# Correct loop with increment
i = 1
while i < 10:
    print("Hello world")
    i = i + 1

# Another example with print done and bye
i = 1
while i <= 3:
    print("Hello world")
    i = i + 1
    print("Done")
    print("Bye")

# Example: Print even numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

print()  # line break

# -------------------------------
# for loop in Python
# A for loop is used to iterate over a sequence (like a range, list, string, etc.)

# Syntax:
# for variable in range(start, stop, step):

# Example: Print numbers from 1 to 19
for i in range(1, 20):
    print(i)

# Example: Print odd numbers from 1 to 19
for i in range(1, 20, 2):
    print(i)

# Example: Print numbers from 10 to 1 (reverse)
# Note: range(start, stop, step) where step must be negative for reverse
for i in range(10, 0, -1):
    print(i)

# -------------------------------
# When to use while loop vs for loop?

# Use a while loop when:
# - You don't know in advance how many times to run the loop
# - You want to run until a condition becomes False

# Use a for loop when:
# - You know exactly how many times to run the loop
# - You are iterating over a sequence (like range, list, tuple, etc.)

# -------------------------------
# Nested Loop
# A nested loop means a loop inside another loop.

# Syntax:
# for outer in range(...):
#     for inner in range(...):
#         code

# Example: Nested for loop
for i in range(1, 4):
    print("Outer loop i =", i)
    for j in range(10, 14):
        print("  Inner loop j =", j)
