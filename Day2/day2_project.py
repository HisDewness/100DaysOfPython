#!/usr/bin/env python3

# This file represents the end of day project 
# presented in day 2 of the Udemy Course for 100 Days of Python

# Tip Calculator Project
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n"))
tip_percentage = float(input("What's the tip percentage?\n"))/100
num_of_people = float(input("How many people will split the bill?\n"))
final_amount = (tip_percentage * (total_bill) + total_bill) / num_of_people
print(f"Each person should pay: ${final_amount:.2f}")