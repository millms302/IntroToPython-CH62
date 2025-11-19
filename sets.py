# Sets are UNORDERED, UNINDEXED, and have NO DUPLICATE

fruits = {
    "apple", "banana", "cherry"
}
print(fruits)

# NO DUPLICATES

fruits= {
    "apple", "banana", "apple"
}
print(fruits)

# Check if an item exists.
print("banana" in fruits)

# add an item
fruits.add("orange")
print(fruits)

# Add multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# remove an item

fruits.remove("banana")
print(fruits)

# If you're not sure an item exists, use (discard to avoid errors)
fruits.discard("papaya")

# Set operations
set1 = {
    1, 2, 3, 4
}
set2 ={ 
    3, 4, 5, 6
}
print(set1.union(set2)) # Combine with no dupes.
print(set1.intersection(set2)) # common elements; returns the dupes
print(set1.difference(set2)) #only returns what is unique to set1