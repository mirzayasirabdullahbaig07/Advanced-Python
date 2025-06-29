#   The print() function outputs objects to the screen (standard output)
#   It can also write to a file‑like text stream via the `file` parameter.

# Simple usage: prints text, then a newline by default
print("Mirza Yasir Abdullah Baig")

# Consecutive print() calls each start on a new line
print("Mirza Yasir Abdullah Baig")
print("The Yasir is a software engineer")

# —— Controlling the line ending ——  
# By default, print() ends with '\n' (newline).  
# Use the `end` parameter to replace it:
print("Yasir", end=" ")    # no newline, just a space
print("Abdullah")           # continues on same line

# —— Mixing data types ——  
# print() will convert any data to string and separate by a space by default
print("Yasir", 24, 3.12, True)

# —— Custom separator ——  
# By default, print() puts a space between items.  
# Use `sep` to choose your own separator:
print("Yasir", "Abdullah", "Baig")               # Yasir Abdullah Baig
print("Abdullah", "Baig", "Software Engineer", sep="/")
# Output: Abdullah/Baig/Software Engineer/Developer

# —— Combining sep and end ——  
print("A", "B", "C", sep=" | ", end=" <<< End of Line\n")
print("Next line starts here")
