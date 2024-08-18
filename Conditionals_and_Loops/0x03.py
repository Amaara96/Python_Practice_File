#!/usr/bin/python3

"""Login autentication"""

username = "admin"
password = "Smartfool"

print("Welcome to my website")
user_username = input("Username: ").lower()
user_password = input("Password: ")

if (user_username == username and user_password == password):
    print("Succesfully logged in")
elif (user_username == username):
    print("Wrong Password")
else:
    print("Incorrect username check password")
