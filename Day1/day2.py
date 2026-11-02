#!/usr/bin/env python3

# This file represents the exercises presented in day 2 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

# Data Types: Strings + String Manipulation

# Printing nth character of a string ("Subscripting")
print("Hello!"[0])

# Printing the last character of a string
print("Hello!"[-1])
# or
print("Hello!"[len("Hello!") - 1])
# or you save initial string and use len() to grab last char
hello_str = "Hello!"
print(hello_str[len(hello_str) - 1])

# String concatenation
print("123" + "345")

# Integers
# Variables in Python must be instantiated, but don't need to have their
# final value set immediately
answer = 123 + 345

# Integers can have commas, but you use underscores to make it readable
print(123_456_789)

# Floats
print(3.14)

# Booleans
# The usual - true or false
the_truth = True
print(the_truth)

# Using the type() function to check the data type of a variable
print(type("whoah"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion ("typecasting")
print(int("123") + int("456"))
# James = 5
print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

#------------------------------------------------------------------------#

# Mathematical Operations in Python
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5) # Division always returns a float
print(3 ** 5) # Exponentiation - N to the power of M
print(3 // 5) # Floor Division - returns the largest integer less than or equal to the result of the division


#------------------------------------------------------------------------#




