#!/usr/bin/env python3

# This file represents the exercises presented in day 4 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

# Importing the random module & a custom made module
import random
import my_module

# Printing / using a custom made module
# "import" + [name_of_file].py
print(my_module.the_greatest_number)

# Accessing a function from a custom module
my_module.who_is_at_the_function()

#------------------------------------------------------------------------#

# Randomization and Python Lists

# Generating a random number between a and b (inclusive)
rand_int = random.randint(1, 10)
print(rand_int)

# Creating random floating point numbers
# random.random() generates a number between 0.0 and 1.0 (excluding 1.0)
rand_0_to_1_exclude_1 = random.random()
# Printing the variable with 7 digits of accuracy
print(f"{rand_0_to_1_exclude_1:.7f}")

# random.uniform() generates a number between 0.0 and 1.0 including both ends
rand_0_to_1 = random.uniform(1, 10)
print(rand_0_to_1)

#------------------------------------------------------------------------#

# Coin Flip "program"

# A coin has two sides, a and b
# The chance of landing on a OR b is 1/2
# If a random number generated is .5 or higher, the coin lands heads
coin_flip = random.uniform(0.0, 1.0)
if(coin_flip >= 0.5):
    print(f"It was {coin_flip}!")
    print("It landed on heads!")
else:
    print(f"It was {coin_flip}!")
    print("It landed on tails!")

# Alternate solution
# Just check if it's 0 or 1 lmao
coin_flip_alt = random.randint(0,1)
if(coin_flip_alt >= 0.5):
    print(f"It was {coin_flip}!")
    print("It landed on heads!")
else:
    print(f"It was {coin_flip}!")
    print("It landed on tails!") 

#------------------------------------------------------------------------#

# Lists in Python
# Comma separated list surrounded by brackets
fruits = [1, 2, 3]
states_of_america = ["California", "Washington", "Virginia"]

# Printing items of a list
# The order in the list is retained and important
# Lists are 0 indexed
print(states_of_america[1])
print(states_of_america[-1])    # the last item of a list

# Changing an item of a list to a new value
states_of_america[1] = "Washington D.C."

# Adding an item to a list
# .append() adds an item to the end of the list (every time)
states_of_america.append("The Land of Cherry")

# Removing an item from a list
# .remove(x) removes the first item with value x from the list
states_of_america.remove("The Land of Cherry")

# Popping an item from a list
# .pop([i]) removes an item at position [i], or the last element
# if [i] is not present
states_of_america.pop()
states_of_america.pop(0)

#------------------------------------------------------------------------#

# Who pays the bill?
# Generate a random name from the group of friends to pay the bill

# Establish a list of names
bums = ["Tommy", "Marcel", "Pia", "Zac"]
unlucky_bum = bums[random.randint(0,3)]
print(f"The unlucky bum is {unlucky_bum}!")

# Alternate solution - .choices()
print(f"{random.choice(bums)} was chosen!")

#------------------------------------------------------------------------#

# IndexOutOfRange error
# Literally what I know already
# Attempting to access an index position that the list doesn't have
# Remember that the len(list[]) is elements+1
print(bums[100])

# Nested lists
cities_list = ["LA", "NYC"]
states_list = ["CA", "NY"]
important_places = [cities_list, states_list]

# Printing positions with a nested list

# The first num tells us which list is being called (0 indexed)
# The second num tells us which element of that list is called
print(important_places[1][0])
