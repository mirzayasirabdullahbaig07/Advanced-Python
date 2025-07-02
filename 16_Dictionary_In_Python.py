# -----------------------------
# What is a Dictionary in Python?
# -----------------------------
# A dictionary is an unordered, mutable, and indexed collection.
# It stores data in key-value pairs.

# Syntax: { key: value }

# -----------------------------
# Why Do We Use Dictionaries?
# -----------------------------
# - Fast data retrieval using keys
# - Meaningful key-value mapping
# - Efficient data organization

# -----------------------------
# Creating Dictionaries (Examples)
# -----------------------------
empty_dict = {}
print("Empty dictionary:", empty_dict)

simple_dict = {"name": "Yasir", "age": 24, "role": "ML Engineer"}
print("Simple dictionary:", simple_dict)

mixed_dict = {1: "One", 2: [1, 2, 3], 3: {"nested": True}}
print("Mixed dictionary:", mixed_dict)

# Using dict() constructor
user = dict(name="Ali", age=30, country="Pakistan")
print("Using dict():", user)

# -----------------------------
# Accessing Items
# -----------------------------
print(simple_dict["name"])          # Yasir
print(simple_dict.get("role"))       # ML Engineer
print(simple_dict.get("salary", 0)) # Default value if key doesn't exist

# -----------------------------
# Adding and Updating Key-Value Pairs
# -----------------------------
simple_dict["experience"] = 2          # Add new key-value
simple_dict["age"] = 25                # Update existing key
print("After add/update:", simple_dict)

# -----------------------------
# Removing Key-Value Pairs
# -----------------------------
del simple_dict["role"]                 # Remove specific key
print("After deletion:", simple_dict)

removed = simple_dict.pop("experience") # Remove and return value
print("Popped value:", removed)

simple_dict.clear()                    # Remove all items
print("Cleared dictionary:", simple_dict)

# -----------------------------
# Iterating Over Dictionary
# -----------------------------
data = {"name": "Yasir", "field": "AI", "level": "Advanced"}

# Keys
for key in data:
    print("Key:", key)

# Values
for value in data.values():
    print("Value:", value)

# Key-Value Pairs
for key, value in data.items():
    print(f"{key} => {value}")

# -----------------------------
# Dictionary in Dictionary (Nested)
# -----------------------------
students = {
    "student1": {"name": "Yasir", "age": 24},
    "student2": {"name": "Ali", "age": 22},
    "student3": {"name": "Ahmed", "age": 25}
}

# Accessing nested values
print(students["student1"]["name"])  # Yasir

# Iterating nested dictionaries
for student_id, info in students.items():
    print(student_id)
    for key, value in info.items():
        print(f"  {key}: {value}")