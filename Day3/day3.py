#!/usr/bin/env python3

# This file represents the exercises presented in day 3 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

# Conditional Statements, Logical Operators, Code Blocks and Scope

# If conditional
if False:
    print("you did a thing")
else:
    print("you did a different thing")

# Example: If a person's height is over 6 feet, they can ride the ride
print("Welcome to the ride!")
height = int(input("What's your height big fella?"))
if height > 6:
    print("You can ride!")
else:
    print("Sorry man!")

# Comparison Operators
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to (exact value, no type check)
# != not equal to

#------------------------------------------------------------------------#

# Modulo Operator
# Returns the remainder from a division operation
print(10%2) # 0, bc 10/2 = 5 w/ NO remainder
print(10%3) # 1, bc 10/3 = 3 w/ ONE remainder (literally 1)

# Even or Odd
usr_input = int(input("Give me your favorite number!\n"))
if usr_input % 2 > 0:
    print("An odd number!")
else:
    print("An even number!")

#------------------------------------------------------------------------#

# Nested if & elif Statements

# Nested if and else statements
# if condition:
    # if another_condition:
        # do thing X
    # else:
        # do thing Y
# else:
    # do thing Z

# elif version
# if condition_one:
    # do thing X
# elif condition_two:
    # do thing Y
# else:
    # do thing Z

# Previous example but more conditions baked in (elif usage)
print("Welcome to the ride!")
age = int(input("What's your age big fella?\n"))
if age > 21:
    print("You can ride no problem!")
elif 13 >= age <= 20:
    print("You can ride but make sure your parent is near!")
else:
    print("Sorry fam, gotta be above a certain age!")

#------------------------------------------------------------------------#

# Coding Exercise 5: BMI Calculator w/ Interpretations
# Add statements so the following is true:
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
weight = 85
height = 1.85
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25.0:
    print("normal weight")
else:
    print("overweight")

#------------------------------------------------------------------------#

# Pizza Order Example
# Based on user order, work out the funal bill
# S/M/L pizza size ($): 15/20/25
# Extra pepp: $2
# Extra cheese: $3
print("Welcome to Python Pizza Parlor!")
size = input("What size pizza? S/M/L: ")
pepperoni = input("You want pepperoni? Y/N: ")
extra_cheese = input("Extra cheese? Y/N: ")

total_price = 0

if  size.lower() == "s":
    total_price +=15
elif size.lower() == "m":
    total_price += 20
else:
    total_price = 25

if pepperoni.lower() == "y":
    total_price += 2
if extra_cheese.lower() =="y":
    total_price+=3

print(f"Your final bill is: ${total_price}")

#------------------------------------------------------------------------#

# Logical Operators

# A and B: both need to be true to return True
# C or D: one needs to be true to return True
# not E: E needs to resolve to false to return True
    # not True = False
    # not False = True

# Checking for age to be BETWEEN two values
# The direction of the signs has to "point" the same
if age < 12:
    print("Child tickets are $5!")
elif 13 <= age <= 20:
    print("You can ride but make sure your parent is near!")
else:
    print("Sorry fam, gotta be above a certain age!")

# Checking if the current value is bigger than the two neighbors
prev = 1
current = 0
next = 2
if prev < current > next:
    print("local maximum")

