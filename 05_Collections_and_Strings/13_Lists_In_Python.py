
# What are Lists?
# -------------------------------
#  Lists are sequence data types in Python that can store multiple values in a single variable.
#  Lists are mutable (modifiable) and can hold elements of different types (int, float, str, etc.)
#  They are similar to arrays but more flexible.

# Creating an empty list
my_list = []

# Creating a list with mixed data types
list1 = [1, 2, 3, "Yasir", True, 0.7]
print(list1)  # Output: [1, 2, 3, 'Yasir', True, 0.7]

# -------------------------------
# Accessing Elements from a List
# -------------------------------
x = [45, 43, 2, 1, 345, 5, 3]

print(x[2])       # Output: 2 (3rd element, index starts from 0)
print(len(x))     # Output: 7
print(x[-1])      # Output: 3 (last element using negative indexing)
print(type(x[2])) # Output: <class 'int'>

# IndexError Examples
# Uncommenting below will throw an error
# print(x[-10])   # IndexError: list index out of range
# print(x[100])   # IndexError: list index out of range

# -------------------------------
# Iterating Through a List
# -------------------------------

# 1. By index
a = [1, 2, 43, 54, 5, 5, 6, 67, 4]
for i in range(len(a)):
    print(a[i])  
# Output: 1 2 43 54 5 5 6 67 4 (each on a new line)

# 2. By value (cleaner)
for value in a:
    print(value)
# Output: Same as above

# -------------------------------
# Built-in List Functions
# -------------------------------
a = [1, 2, 4, 55, 6, 6, 6, 6]

print("Length:", len(a))    # Output: 8
print("Sum:", sum(a))       # Output: 86
print("Max:", max(a))       # Output: 55
print("Min:", min(a))       # Output: 1

# Why use these?
# These functions help summarize data quickly: useful in analysis, loops, or conditions.

# -------------------------------
# Mutable vs Immutable
# -------------------------------
# Mutable: Can be changed after creation (e.g., lists, dictionaries)
# Immutable: Cannot be changed after creation (e.g., strings, tuples)

# -------------------------------
# List Methods (with Definitions & Examples)
# -------------------------------

my_list = [10, 20, 30, 40]

# 1. append(x): Adds item to the end
my_list.append(50)
print("After append:", my_list)  # [10, 20, 30, 40, 50]

# 2. insert(i, x): Inserts at position i
my_list.insert(2, 25)
print("After insert:", my_list)  # [10, 20, 25, 30, 40, 50]

# 3. extend(iterable): Adds multiple values
my_list.extend([60, 70])
print("After extend:", my_list)  # [10, 20, 25, 30, 40, 50, 60, 70]

# 4. remove(x): Removes first occurrence of x
my_list.remove(25)
print("After remove:", my_list)  # [10, 20, 30, 40, 50, 60, 70]

# 5. pop(i): Removes and returns item at index i (default last)
my_list.pop()  
print("After pop():", my_list)  # [10, 20, 30, 40, 50, 60]
my_list.pop(1)
print("After pop(1):", my_list)  # [10, 30, 40, 50, 60]

# 6. index(x): Returns first index of x
print("Index of 30:", my_list.index(30))  # 1

# 7. count(x): Counts occurrences of x
print("Count of 10:", my_list.count(10))  # 1

# 8. sort(): Sorts in ascending order
num_list = [5, 2, 9, 1, 7]
num_list.sort()
print("After sort:", num_list)  # [1, 2, 5, 7, 9]

# 9. reverse(): Reverses the list
num_list.reverse()
print("After reverse:", num_list)  # [9, 7, 5, 2, 1]

# 10. copy(): Returns a shallow copy
copied_list = num_list.copy()
print("Copied list:", copied_list)  # [9, 7, 5, 2, 1]

# 11. clear(): Empties the list
copied_list.clear()
print("After clear:", copied_list)  # []

# -------------------------------
# List Comprehension
# -------------------------------
# A compact way to generate or transform lists

# Basic usage
my_list = [i for i in range(1, 21)]
print(my_list)  # [1, 2, ..., 20]

# Same value for all
my_list = ["even" for i in range(1, 21)]
print(my_list)  # ['even', 'even', ..., 'even']

# Remainder of division by 2
my_list = [i % 2 for i in range(1, 21)]
print(my_list)  # [1, 0, 1, 0, ..., 0]

# Conditional expression (even/odd)
my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 21)]
print(my_list)
# Output: ['odd', 'even', 'odd', ..., 'even']

# Filter even numbers only
my_list = [i for i in range(1, 21) if i % 2 == 0]
print(my_list)  # [2, 4, 6, ..., 20]

# Divisible by both 2 and 3
start = int(input("Enter start number = "))  # e.g. 1
end = int(input("Enter end number = "))      # e.g. 30

my_list = [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 == 0]
print(my_list)  # Output: [6, 12, 18, 24, 30]

# Why use list comprehensions?
#  Cleaner, faster, and concise for transformations, filters, or conditional assignments.

# -------------------------------
# List Slicing
# -------------------------------

# What is Slicing?
# Slicing means extracting a part of the list using the syntax:
# list[start:end:step]

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. Basic slicing
print(nums[0:5])   # [10, 20, 30, 40, 50]
print(nums[:4])    # [10, 20, 30, 40]
print(nums[5:])    # [60, 70, 80, 90, 100]

# 2. Step slicing
print(nums[::2])   # [10, 30, 50, 70, 90]
print(nums[1::2])  # [20, 40, 60, 80, 100]

# 3. Negative slicing (reverse)
print(nums[::-1])  # [100, 90, ..., 10]
print(nums[-3:])   # [80, 90, 100]
print(nums[-5:-2]) # [60, 70, 80]

# Why use slicing?
#  For data cleaning, data extraction, reversing lists, skipping elements, or efficient subsetting

# -------------------------------
# Final Summary
# -------------------------------
#  Lists are essential for managing and manipulating sequences of data.
#  Use methods like append, insert, pop, etc., to modify them.
#  Use list comprehensions for fast, readable logic.
#  Use slicing for powerful subsetting and transformations.
