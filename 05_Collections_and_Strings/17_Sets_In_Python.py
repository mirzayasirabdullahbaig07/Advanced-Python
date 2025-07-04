# -------------------------------------
# PYTHON SETS - COMPLETE EXPLANATION
# -------------------------------------

# 1. What are Sets?
# -----------------
# Sets are unordered collections of unique, immutable elements.
# They do not allow duplicates.
# They are mutable (you can add/remove items).
# They do not support indexing or slicing.

# 2. Creating Sets
# ----------------

# Wrong way to create an empty set
s1 = {}
print(type(s1))  # dict

# Correct empty set
s2 = set()
print(type(s2))  # set

# Creating a set with duplicates
s3 = {1, 2, 2, 3, 4, 5, 5}
print(s3)  # {1, 2, 3, 4, 5} (duplicates removed)

# Mixed data types allowed
s4 = {1, 3.14, "Yasir", True}
print(s4)

# Tuples (immutable) are allowed
s5 = {(1, 2), "AI"}
print(s5)

# Sets inside sets are not allowed (sets are mutable)
# s6 = {{1, 2}, 3}  # ❌ TypeError
# Use frozenset to allow sets inside sets
s6 = {1, 2, frozenset({3, 4})}
print(s6)

# 3. Type Conversion
# ------------------
list_to_set = set([1, 2, 2, 3])
print(list_to_set)  # {1, 2, 3}

str_to_set = set("yasir")
print(str_to_set)   # {'y', 'a', 's', 'i', 'r'} (unordered)

# 4. Modifying Sets
# ------------------
s = {1, 2, 3}
s.add(4)                  # Add item
print(s)
s.update([5, 6])          # Add multiple items
print(s)
s.remove(2)              # Remove item (error if not found)
print(s)
s.discard(10)            # No error if item not found
print(s)
s.pop()                  # Removes random item
print(s)
s.clear()                # Empties the set
print(s)

# 5. Membership Operators
# ------------------------
members = {"yasir", "abdullah", "baig"}
print("yasir" in members)      # True
print("hamza" not in members)  # True

# 6. Looping Through Sets
# ------------------------
loop_set = {1, 2, 3, 4, 5}
for item in loop_set:
    print(item)

# 7. Set Methods
# --------------
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))                   # {1, 2, 3, 4, 5}
print(A | B)

print(A.intersection(B))           # {3}
print(A & B)

print(A.difference(B))             # {1, 2}
print(A - B)

print(A.symmetric_difference(B))   # {1, 2, 4, 5}
print(A ^ B)

# 8. Set Relationships
# ---------------------
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))         # True
print(set2.issuperset(set1))       # True
print(set1.isdisjoint({4, 5}))     # True

# 9. Built-in Functions
# ----------------------
nums = {1, 2, 3, 4, 5}
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sorted(nums))

# 10. Notes
# ----------
# - Sets are ideal for membership testing, uniqueness filtering, and mathematical set operations.
# - Use frozenset if you need an immutable version of a set.
# - Sets are unordered; their printed order may vary.