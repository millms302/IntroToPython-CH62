# Tuples are just like lists - they can store multiple items.
# BUT!!! Tuples are IMUTABLE, you CANNOT change them after you create them. NO EDITTING

my_tuple = (
    "apple", "banana", "cherry"
)
print(my_tuple)

# Accessing items
print(my_tuple[0])
print(my_tuple[2])

# Check is item exists
if "cherry" in my_tuple:
    print("Yes, It is")

# Length of Tuple
print(len(my_tuple))

#Single Item Tuple
single = ("apple")
print(type(single)) #Not a tuple, just a string.
correct = ("correct",) #this is a tuple, must iinclude comma after the item
print(type(correct))

# Nested Tuple
tuple1 = ("a", "b", "c",)
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)
