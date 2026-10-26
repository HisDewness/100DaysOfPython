#!/usr/bin/env python3

# This file represents the exercises presented in day 1 of the Udemy Course for 100 Days of Python

# Beginner
# Working with variables in Python

# Printing a string literal
print("Hello world chief");

# Printing a variable with a string literal
hello_world = "Hello world"
print(hello_world);

# Printing a string literal across 3 lines but using 1 line of code
print("Hello world!\nHello bum\nHello fam");

# String concatenation
print("Hello" + " " + "bruh")

#------------------------------------------------------------------------#

# Coding Exercise 1: Printing Practice

# Write a program that uses print statements to print the following recipe into the Output console. 
# The text to print is already there, you just need to make it into code. Your code should print all 
# five lines exactly the same as the example output below.

# 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# 2. Knead the dough for 10 minutes.
# 3. Add 3g of Salt.
# 4. Leave to rise for 2 hours.
# 5. Bake at 200 degrees C for 30 minutes.

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#------------------------------------------------------------------------#

# Coding Exercise 2: Debugging Practice

# Look at the code in the code editor. There are errors on all 5 lines of code. Fix the code so that it runs without errors.

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

#------------------------------------------------------------------------#

# Coding Exercise 3: Variables

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
# Write 3 lines of code to switch the contents of the variables. You are not allowed to type
# the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp