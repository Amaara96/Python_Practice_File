#!/usr/bin/python3

"""This program implements the for loop"""

"""Prints each character in a string"""
name = input("Name: ")

for ch in name:

    if (ch == "m"):
        continue
    print(ch * 6) #The * symbol multiplies the character

else:
    print("The loop has finished executing")