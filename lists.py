# Lists are used to store MULTPILE items in a single variable.

my_list = [10, 20, 30, 40, 50]
print (my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

# Accessing list items by their INDEX number

fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])

# You can also use NEGATIVE indexes to cout from the end

print(fruits[-1]) 

# MODIFY THE LIST

fruits [1] = "mango"
print(fruits)

# Adding to the list

fruits.append("orange")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

# Removing items

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

# Check if item exists.

if "mango" in fruits:
    print("Yes, mango is in list")

# list length
print(len(fruits)) # Number of items in the list