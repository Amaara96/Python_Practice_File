#!/usr/bin/python3

# Generate Username from first name and surname

fname = input("First Name: ")
surname = input("Surname: ")

#username = 2fname + " " + 3surname

username = fname[0:3] + ' ' + surname[0:3]

# Print the generated username here

print("Your username is: ", username)