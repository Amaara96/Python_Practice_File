#!/usr/bin/python3

# Using the str_format string formatting function(This is a new style formatting)

fname = input("Firstname: ")
surname = input("Surname: ")
age = int(input("Age: "))


# The old style formatting
print("Your name is %s %s and you are %d years old" %(fname, surname, age))

print()

# The new style formatting
print("Your name is {} {} and you are {} years old" .format(fname, surname, age))

#The f-string formatting style
print(f"Your name is {fname:s} {surname:s} and am {age:d}")
