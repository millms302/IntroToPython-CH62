# Operators are like "symbols" or "shortcuts"
# that thell the computer to do something with the values.

# 1) Arithmetic Operator: used with numeric variables, basically a calculator
x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y
print(res)

res = x / y
print(res)

res - x % y # Modulus -> remainder after division

res = x ** y # Exponentation-> x to the power of y
print(res)

res = x//y #floor division-> divide and drop the decimnal
print(res)


print("________________")
# 2) Assignment Operators -  Used to assign values to variables.
# =means "put this calue inside the (variable)"

x =5
x += 0
x -= 3
x *= 3
x /= 3
print(x)

print("_____________________________________")
# 3) Comparison Operator
# used to compare two values
# same as if else
z = 5
p = 5
print(z == p) # E'qual to
print(z != p) # Not equal to
print(x <= p) # less than
print(z >= p) # greater than

print("__________________________________________________")
# 4) Logical Operators
# used to combine conditional statements

x = 3
y = 10
z = 3

print(x == y and y == z) # False, bother conditions are not true
print(x == y or y == z) # True, at least one condition is TRue
print(not x == y) # True because x == y is false.

print("_________________________________")
# 5) Idendtity Operator
# used to compare the objects, not if they are equal
# are actually the same object with the same memory location.

x=3
y=3
print(x is y) # Returns True if bothe variables are the same object.
print(x is not y ) # Returns true if both cariables are not the same object

print("___________________________________")
# 6) Membership Operator
# used to test if a sequence is presented in an object

x = [1, 2, 3, 4, 5] # this is a list.

print(4 in x) # True, 4 is included in the list.
print(9 not in x) #True because 9 is not included in the list.

