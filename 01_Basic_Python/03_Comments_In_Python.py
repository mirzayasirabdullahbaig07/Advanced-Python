#    What are Comments in Python?

# ➤ Comments are lines in your code that are **not executed**.
# ➤ They are written to explain what the code does.
# ➤ Comments make your code **easier to understand** for you and others.
# ➤ Python’s interpreter **completely ignores** comments during execution.

# ----------------------------------------------------------
#   Types of Comments in Python
# ----------------------------------------------------------

#   1. Single-line Comment:
# Use the hash symbol (#)
# Everything after # on that line is treated as a comment

print("Yasir")  # This is a single-line comment explaining the line

#    2. Multi-line Comments:
# Python doesn’t have built-in multi-line comment symbols like C/C++ (/* */)
# But we can simulate them using triple-quoted strings

"""
This is a multi-line comment.
It uses triple double-quotes.
It is also called a docstring when used at the start of a function or class.
"""

'''
Some developers prefer using triple single quotes.
Both are acceptable for multi-line comments.
'''

#   NOTE: Multi-line comments using triple quotes are not **true** comments.
# They are actually **string literals** — but if not assigned to a variable or used as a docstring, Python will ignore them.

#   3. Inline Comments:
# Comments written on the same line as code

x = 5  # This is an inline comment explaining variable x

# ----------------------------------------------------------
#   Best Practices for Writing Comments
# ----------------------------------------------------------

# ✔ Keep comments short and to the point.
# ✔ Use comments to explain “why” something is done, not just “what”.
# ✔ Don’t overuse comments for obvious code — clean code speaks for itself.
# ✔ Keep your comments updated if your code changes.

# Example of bad vs good comment:

#   Bad comment
x = x + 1  # add 1 to x

#   Good comment
x = x + 1  # increment x to count the next item

# ----------------------------------------------------------
#   Summary:
# - Comments make code easier to understand
# - Python supports single-line and multi-line (via triple quotes) comments
# - They are ignored by the interpreter and don't affect program output
# - Use comments to explain **why**, not just **what**
