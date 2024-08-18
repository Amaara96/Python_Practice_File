#!/usr/bin/python3

"""This is for the while loop"""

counter = 1 #initialization

while (counter <= 10): #condition
    """Will only execute if the condition is true"""
    
    if (counter == 4):
        print("four!")
    elif (counter == 5):
        print("five!")
    else:
        print(counter)
    counter = counter + 1 #This is the increment/decrement

print("The loop finally finished its execution")