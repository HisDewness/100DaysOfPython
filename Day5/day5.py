#!/usr/bin/env python3

# This file represents the exercises presented in day 5 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

# Python Loops

# For loops in Python
# Iterating is simpler than Java or C#
# The type of the element isn't checked at instantiation in the list,
# it's only checked at runtime when an operation is ran on it
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)

# Using a for loop to do the sum() functionality
# total_score = sum(scores)
scores = [1,2,3,4,5]
sum = 0
for curr_score in scores:
    sum += curr_score
print(sum)

# Using a for loop to do the max() functionality
# max() returns the highest value in an iterable list
# If the current max_value is less than the current value,
# set the max_value to that value for now
max_value = 0
for curr in scores:
    if max_value < curr:
         max_value = curr
print(max_value)

#------------------------------------------------------------------------#

# The Range function

# range(a, b) generates a set of numbers between a and b
# range(a, b, c) generates a set of numbers between a and b, in
# interverals of c
for number in range(1, 10):
    print(number) # excludes b, so this would print 1 - 9

# The Gauss Challenge
# Print out the total of all numbers between 1 and 100, inclusive both
total = 0
for num in range(1, 101):
    total += num
print(total)

#------------------------------------------------------------------------#

# Coding Exercise #6: FizzBuzz

# Write a program that prints the solution to FizzBuzz
# Rules
# 1. Print every number from 1 - 100 and include 100
# 2. When number is divisible by 3, print "Fizz"
# 3. When number is divisible by 5, print "Buzz"
# 4. When number is divisible by both, print "FizzBuzz"

print("\nWelcome to FizzBuzz!")

# Iterate through the numbers inclusive of 100
for num in range(1, 101):
    if (num % 3 == 0 and num % 5 == 0):
        print("FizzBuzz")
        # continue
    elif (num % 3 == 0):
        print("Fizz")
        # continue
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)
    
