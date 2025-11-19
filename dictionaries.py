# Dictionaries store data in KEY:VALUE pairs. Just like a real dictionary with WORD:DEFINITION
students = {
    "name": "Mike",
    "age": 33,
    "major": "computer science"
}

print(students)

# Accessing Items
print(students["name"]) # Access by Key
print(students.get("major")) # Access another way (.get)

# Add new item
students["graduation year"] = 2025
print(students) # Always adds at the end

# Changing Values
students["age"] = 23
print(students)

# Remove Item
students.pop("major")
print(students)

# Check if an item exists
if "name" in students:
    print("Key 'name' is in the dictionary")

# Nested dictionary
stuedents = {
    "student1" : {"name": "Mike", "age": 20},
    "student2": {"name": "Alex", "age": 30}
}
print(stuedents["student1"]["name"])

