# ----------------------------------
# What Are Tuples in Python?
# ----------------------------------
# Tuples are similar to lists, but with one key difference:
#  Tuples are immutable — once created, their content cannot be changed.
#  Tuples support indexing, slicing, iteration, and nesting.
#  They have only 2 methods: count() and index()

# ----------------------------------
# Creating Tuples
# ----------------------------------
tuple1 = ()
print("Empty tuple:", tuple1)

tuple2 = (1, 2, 3, 4)
print("Tuple with integers:", tuple2)

tuple3 = (1, 2, 3, "Yasir", True)
print("Heterogeneous tuple:", tuple3)

# Single item tuple - comma is mandatory
tuple4 = (1,)
print("Single element tuple:", tuple4)

# Creating tuple from string
tuple5 = tuple("Yasir")
print("Tuple from string:", tuple5)

# Creating tuple from list
tuple6 = tuple([1, 2, 3, 4, 5, 6])
print("Tuple from list:", tuple6)

# ----------------------------------
# Accessing Tuple Elements
# ----------------------------------
tuple11 = (1, 2, 3, 5, 6)
print("Element at index 1:", tuple11[1])
print("Second last element:", tuple11[-2])

# Nested tuple
tuple22 = (1, 2, 3, (4, 5))
print("Accessing nested tuple element:", tuple22[-1][0])

# ----------------------------------
# Tuple Immutability
# ----------------------------------
deltuple = (1, 2, 3, 4, 5)
print("Original tuple:", deltuple)

# Uncomment below to delete entire tuple variable
# del deltuple

# ----------------------------------
# Tuple Operations
# ----------------------------------
tup1 = (1, 2)
tup2 = (3, 4)

# Concatenation
print("Concatenated:", tup1 + tup2)

# Repetition
print("Repeated tup1:", tup1 * 2)
print("Repeated tup2:", tup2 * 3)

# Looping through tuple
print("Elements in tup1:")
for i in tup1:
    print(i)

# Membership testing
print("Is 1 in tup1?", 1 in tup1)
print("Is 3 in tup1?", 3 in tup1)
print("Is 1 not in tup1?", 1 not in tup1)

# ----------------------------------
# Tuple Built-in Functions
# ----------------------------------
functup = (1, 2, 2, 4, 54, 65, 6)

print("Length:", len(functup))
print("Minimum value:", min(functup))
print("Maximum value:", max(functup))
print("Sorted (ascending):", sorted(functup))              # returns a list
print("Sorted (descending):", sorted(functup, reverse=True))

# ----------------------------------
# Summary
# ----------------------------------
#  Tuples are immutable (read-only)
#  Lists are mutable (read-write)
#  Tuples use less memory and are faster for fixed data
#  Good for protecting data integrity
