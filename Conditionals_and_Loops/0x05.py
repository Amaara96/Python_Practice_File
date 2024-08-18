#!/usr/bin/python3

"""Using the continue function"""

counter = 1 #initialization

while (counter <= 10): #condition
    """Will only execute if the condition is true"""
    
    if (counter == 4):
        counter = counter + 1
        continue #This allows the loop to skip this particular number
    elif (counter == 5):
        print("five!")
    else:
        print(counter)
    counter = counter + 1 #This is the increment/decrement

print("The loop finally finished its execution")