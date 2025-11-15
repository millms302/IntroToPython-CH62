""""""
print("hello world from Python")
print(2)
print(2+3)
print(True)
""""""
# This is a comment. Never Executed in the Terminal, For my notes.
"""
This is a multiline comment
"""

#create a variable
name = "Michael"
age = 33
middle_name = "Tyranasaurus"
last_name = "Miller"
found = False
print(name)

# concantination (putting things together all happy family like.)
print("My name is: " + name + ", and  I am " + str(age) + " years old." + middle_name)
print("Did He Show Up To Class" + str(found))

# F Format
# f"" or f"""""""
print(f"My name is: {name}, and I am {age} years old.")
print(f""" 
Mike
      lalala
    middle{middle_name}
                printing
      
""")

# type() function helps us to know what type of data the variable is
print(type(name))
print(type(age))
print(type(found))

# Casting: 
# Helps us convert to different data types.
print(20+int("20"))
print(20+age)

# Input Method
# Is going to allow us to interact with the terminal to pass some variables.
# print(input("Enter Your Name:"))
# print(type(input("enter your name here: ")))

#new_age = (input("Enter your age here: "))
#print(new_age + age)
#print(str(age) + new_age)

x  = int(input("enter first value: "))
y = int(input("enter the second value: "))
print(x+y)