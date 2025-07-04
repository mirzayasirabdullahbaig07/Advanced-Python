# What are Control Statements in Python?
# Control statements are an essential aspect of any programming language, including Python.
# They are used to manage the flow of execution in a program based on certain conditions.

# Python Control Statements:
# 1. break
# 2. continue
# 3. pass

# -------------------------------------
# 1. break statement
# The break statement is used to terminate the loop immediately when a certain condition is met.

print("Example 1: break after printing 5")
for i in range(1, 11):
    print(i)
    if i == 5:
        break  # Output: 1, 2, 3, 4, 5

print("Example 2: break before printing 5")
for i in range(1, 11):
    if i == 5:
        break
    print(i)  # Output: 1, 2, 3, 4

# -------------------------------------
# 2. continue statement
# The continue statement is used to skip the current iteration and move to the next one.

print("Example: skip when i == 5")
for i in range(1, 11):
    if i == 5:
        continue  # Skips printing 5
    print(i)
    print("Yasir")

# -------------------------------------
# 3. pass statement
# The pass statement does nothing. It is a placeholder used when a statement is syntactically required,
# but you don’t want to write any code yet.

print("Example: using pass in a loop")
for i in range(1, 6):
    if i == 3:
        pass  # You may want to add some logic here later
    print(i)

# Note:
# - break: stops the loop
# - continue: skips the current iteration
# - pass: does nothing (used as a placeholder for future code)
