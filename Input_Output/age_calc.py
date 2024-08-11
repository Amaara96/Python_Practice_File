#!/usr/bin/python3

"""This program converts different type of integers(type conversions)"""
# This is an age calculator

# Place your Date of Birth
year_of_birth = input("What year were you born?: ")
Month_of_birth = input("What is the month of birth(0 - 12): ")
Day_of_birth = input("Please give me date: ")

# Place the current year
current_year = input("What year are you in?: ")

# Calculate the year
age = int(current_year) - int(year_of_birth)

print("Your date of birth is ", end=" ")
print(Day_of_birth, "-", Month_of_birth, "-", year_of_birth)

#displays the age
print("You are ", age, end=" ")
print("years old", end="\n")