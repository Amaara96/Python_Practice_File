#!/usr/bin/python3

"""This is a python file thay utilizes the elif statements and logical 
operators."""

"""Give us direction on the traffic light"""

light = input("What color is the light: ")

if (light.lower() == "red"):
    print("Hey stop")

elif (light.lower() == "yellow"):
    print("Get ready")

elif (light.lower() == "green"):
    print("go!")

else:
    print ("This color does not exist on the traffic light")