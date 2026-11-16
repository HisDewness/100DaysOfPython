#!/usr/bin/env python3

# This file represents the end of day project 
# presented in day 5 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

import random

# Password Generator Project
# Easy level - generate the values in sequence
# Hard level - generate the values out of sequence

# Establish the lists for what we need for a good password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while(True):
    final_pass = ""
    # Start the shenanigans
    print("\nWelcome to the password generator project!")

    # Ask user for input (how many of each)
    num_letters = int(input("How many letters?\n"))
    num_numbers = int(input("How many numbers?\n"))
    num_symbols = int(input("How many symbols?\n"))

    total_characters = (num_letters + num_numbers + num_symbols)

    # We need total_characters to be greater than 0
    if (total_characters < 1):
        print("We can't make a password with less than one character fam")
    else:
        # Establish list subsets
        chars_chosen = []
        # For the number of letters chosen, iterate that many times
        # then add to subset list of letters randomly
        for curr in range(0, (num_letters)):
            chars_chosen.append(random.choice(letters))
        for curr in range(0, (num_numbers)):
            chars_chosen.append(random.choice(numbers))
        for curr in range(0, (num_symbols)):
            chars_chosen.append(random.choice(symbols))
        # Print the everything together
        # .sample(original_list, length of new list) shuffles the original list
        # into a new list while retaining the original 
        final_pass = "".join(random.sample(chars_chosen, len(chars_chosen)))
        print(f"Your final password is: {final_pass}")