

# --------------------------------------------
# What is File Handling?
# --------------------------------------------
# File handling in Python refers to the ability to read, write, create, delete,
# and manipulate files stored on your computer (like .txt, .csv, .json files).

# --------------------------------------------
# Why We Use File Handling?
# --------------------------------------------
# - To store data permanently (unlike variables which lose value after program ends)
# - To read logs, user input, config files
# - To work with datasets, save reports or export results

# --------------------------------------------
# File Modes
# --------------------------------------------
# 'r'  - read (default, file must exist)
# 'w'  - write (overwrites if exists or creates new)
# 'a'  - append (adds at the end)
# 'x'  - create (error if file exists)
# 'r+' - read and write
# 'b'  - binary mode (e.g., 'rb', 'wb')

# --------------------------------------------
# Basic Examples
# --------------------------------------------

# Write to file
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")

# Append to file
with open("example.txt", "a") as f:
    f.write("Another line.\n")

# Read from file
with open("example.txt", "r") as f:
    data = f.read()
    print(data)

# Read line-by-line
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# --------------------------------------------
# Exception Handling (try-except)
# --------------------------------------------

try:
    with open("nofile.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print(" File not found.")
except PermissionError:
    print(" Permission denied.")
else:
    print(" File read successfully.")
finally:
    print(" Operation completed (with or without error).")

# --------------------------------------------
# Logical Error Example
# --------------------------------------------
# Overwriting data instead of appending:
with open("log.txt", "w") as f:
    f.write("This deletes previous content!\n")  # Logical mistake

# Correct:
with open("log.txt", "a") as f:
    f.write("This keeps previous content.\n")

# --------------------------------------------
# Multiple Exception Handling
# --------------------------------------------

try:
    with open("data.txt", "r") as file:
        print(file.read())
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")

# --------------------------------------------
# File Operations (Create, Delete, Move)
# --------------------------------------------

import os

# Create a new file (x mode)
try:
    with open("newfile.txt", "x") as f:
        f.write("Created new file.")
except FileExistsError:
    print("File already exists.")

# Delete a file
if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("File deleted.")
else:
    print("File does not exist.")

# Rename or move a file
os.rename("example.txt", "renamed_example.txt")  # Rename

# --------------------------------------------
# Read Methods
# --------------------------------------------
# read()     -> Reads entire content as string
# readline() -> Reads one line
# readlines() -> Reads all lines as list

with open("renamed_example.txt", "r") as f:
    print(f.readline())
    print(f.readlines())

# --------------------------------------------
#  Important Tips
# --------------------------------------------
#  Always use `with open(...)` — auto-closes file safely
#  Use exception handling to prevent crash
#  File paths: use relative (./folder/file.txt) or absolute (C:/folder/file.txt)
#  Always close files if not using `with`

# --------------------------------------------
#  Summary
# --------------------------------------------
# - File handling enables persistent data storage
# - Modes: r, w, a, x, r+
# - Always handle exceptions (FileNotFoundError, etc.)
# - Perform safe file operations (read, write, delete, rename)
# - Use try-except-else-finally for robust programs

# This guide covers all foundational file handling concepts in Python.
