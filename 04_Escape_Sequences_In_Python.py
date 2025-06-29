# Escape Characters / Escape Sequences in Python

# ➤ Escape characters are special characters that **start with a backslash `\`**
# ➤ They are used to insert characters into a string that are **otherwise illegal or unprintable**
# ➤ Python uses the backslash `\` to escape the next character

# Common Escape Sequences with Simple Examples:

# 1. \' → Single Quote
print('It\'s a beautiful day!')  # Output: It's a beautiful day!

# 2. \" → Double Quote
print("She said, \"Hello!\"")    # Output: She said, "Hello!"

# 3. \\ → Backslash
print("This is a backslash: \\")  # Output: This is a backslash: \

# 4. \n → New Line
print("Line 1\nLine 2")  # Output: 
# Line 1
# Line 2

# 5. \t → Tab (adds horizontal space like a tab key)
print("Name:\tYasir")  # Output: Name:    Yasir

# 6. \b → Backspace (deletes one character space before it)
print("Helloo\b!")  # Output: Hello!

# ----------------------------------------------------------
# Summary:
# - Escape sequences help include special characters in strings
# - Always begin with a backslash `\`
# - They help format strings in a readable way

# Tip:
# If you don't want Python to treat backslashes as escape characters, use **raw strings**:
print(r"This will print the backslash: \n\t\\")  # Output: This will print the backslash: \n\t\\
