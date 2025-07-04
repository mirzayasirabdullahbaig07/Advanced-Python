# --------------------------------------------------
# 01. What Are Strings in Python?
# --------------------------------------------------
# Strings are sequences of Unicode characters.
# Example: "Yasir" = 'Y', 'a', 's', 'i', 'r'

# --------------------------------------------------
# 02. Creating Strings
# --------------------------------------------------
a = 'Mirza Yasir Abdullah Baig'  # Single quotes
print(a)

b = "Mirza Yasir Abdullah Baig"  # Double quotes
print(b)

c = "It's raining outside"       # Double quotes handle single quote inside
print(c)

d = """Yasir is an AI developer and a machine learning expert"""  # Triple quotes
print(d)

e = '''Used for multi-line strings or paragraphs (e.g. blogs)'''
print(e)

f = str("Mirza Yasir Abdullah Baig")  # Using str() constructor
print(f)

# --------------------------------------------------
# 03. Accessing String Characters (Indexing)
# --------------------------------------------------
name = "YASIR"
print(name)

# Positive Indexing
print(name[0])  # Y
print(name[1])  # A
print(name[2])  # S
print(name[3])  # I
print(name[4])  # R
# print(name[5])  # Error: Index out of range

# Negative Indexing
print(name[-1])  # R
print(name[-2])  # I
print(name[-3])  # S
print(name[-4])  # A
print(name[-5])  # Y

# --------------------------------------------------
# 04. Slicing Strings
# --------------------------------------------------
text = "Mirza Yasir Abdullah Baig"
print(text[0:6])         # 'Mirza '
print(text[2:])          # 'rza Yasir Abdullah Baig'
print(text[:5])          # 'Mirza'
print(text[:])           # Full string
print(text[0:6:2])       # 'Mra'
print(text[-6:-1:2])     # ' B'
print(text[::-1])        # Reversed string
print(text[-1:-7:-1])    # Last 6 characters reversed

# Invalid slice direction
# print(text[0:7:-1])    # Empty string (invalid direction)

# --------------------------------------------------
# 05. Editing & Deleting Strings
# --------------------------------------------------
s = "AI Machine Learning Journey"
# s[0] = "X"  # Error: Strings are immutable
print(s)

# Reassigning is allowed
s = "AI Courses"
print(s)

# Deleting specific character not allowed
# del s[0]

# Entire string deletion is allowed
del s
# print(s)  # Error: s is deleted

# --------------------------------------------------
# 06. String Operators
# --------------------------------------------------

# Arithmetic Operators
str1 = "Yasir"
str2 = "Baig"
print(str1 + " " + str2)     # Concatenation
print(str1 * 3)              # Repetition

print("*" * 40)

# Relational Operators (Lexicographical)
print("yasir" == "baig")
print("Abdullah" != "Mirza")
print("Islamabad" > "Kasur")  # False because I < K
print("Yasir" > "yasir")      # False because uppercase < lowercase

# Logical Operators
print("Yasir" and "Baig")   # Returns last truthy: 'Baig'
print("Yasir" or "Baig")    # Returns first truthy: 'Yasir'
print("" and "Baig")        # Empty string is falsy
print("" or "Baig")         # Returns 'Baig'

# --------------------------------------------------
# 07. Looping in Strings
# --------------------------------------------------
for char in "Mirza Yasir Abdullah Baig":
    print(char)

# --------------------------------------------------
# 08. Membership Operators
# --------------------------------------------------
s = "Mirza Yasir Abdullah Baig"
print('M' in s)       # True
print('Z' not in s)   # True

# --------------------------------------------------
# 09. Common String Functions
# --------------------------------------------------
str_func = "Mirza Yasir Abdullah Baig"

print(len(str_func))
print(max(str_func))  # Based on ASCII (space < caps < lowercase)
print(min(str_func))
print(sorted(str_func))               # Returns sorted list
print(sorted(str_func, reverse=True))  # Descending

# --------------------------------------------------
# 10. String-Specific Methods
# --------------------------------------------------
example = "mirza yasir abdullah baig"

print(example.capitalize())  # First letter uppercase
print(example.title())       # Each word capitalized
print(example.upper())       # All uppercase
print(example.lower())       # All lowercase
print(example.swapcase())    # Swap cases
print(example.count("a"))    # Count occurrence
print(example.find("y"))     # Returns -1 if not found
# print(example.index("Z"))  # Crashes if not found

print(example.startswith("mirza"))
print(example.endswith("baig"))

# --------------------------------------------------
# 11. Format Function
# --------------------------------------------------
print("My name is {} and I am {}, age {}".format("Yasir", "AI/ML Engineer", 24))
print("My name is {0}, I am {1}, age {2}".format("Yasir", "AI/ML Engineer", 24))
print("My name is {name}, I am {status}, age {age}".format(name="Yasir", status="AI/ML Engineer", age=24))

# --------------------------------------------------
# 12. String Validation Functions (is*)
# --------------------------------------------------
print("yasir07".isalnum())       # True
print("yasir07#".isalnum())      # False
print("yasir".isalpha())         # True
print("123".isdigit())           # True
print("7A".isdigit())            # False
print("Yasir_Baig".isidentifier())   # True
print("Yasir-Baig".isidentifier())   # False

# --------------------------------------------------
# 13. split() and join()
# --------------------------------------------------
line = "Mirza Yasir Abdullah Baig"
print(line.split())              # By default, space
print(line.split("i"))           # Split by 'i'
print(line.split("x"))           # No split

# Join example
names = ['Mirza', 'Yasir', 'Abdullah', 'Baig']
print("-".join(names))           # 'Mirza-Yasir-Abdullah-Baig'

# --------------------------------------------------
# 14. replace(), strip()
# --------------------------------------------------
print("mirza yasir abdullah".replace("abdullah", "baig"))

# strip() removes leading and trailing spaces
strip_example = "   Hello Yasir     "
print(strip_example.strip())   # "Hello Yasir"
