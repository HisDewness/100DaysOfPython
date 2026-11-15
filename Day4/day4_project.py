#!/usr/bin/env python3

# This file represents the end of day project 
# presented in day 4 of the Udemy Course for 100 Days of Python

#------------------------------------------------------------------------#

import random

# Rock Paper Scissors Project
# Build a rock, paper, scissors game using what was learned
# with randomization and lists in Python

# Plan
# Establish choice variables w/ ascii art
# Establish lists of elements
# Ask user for input of choice (0/1/2 for R/P/S)
# Randomize computer's choice from list
# Use if + else to determine winner
# Print results

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Establish list of options (both player and user can use these)
game_options = [rock, paper, scissors]

while True:
    # Get player choice, converting to int so list position can be used for elements
    player_decision = int(input("What do you choose?\nRock, Paper, or Scissors? (0, 1, 2)\n"))
    player_choice = game_options[player_decision]

    # Print out the first choice used by the player
    print(f"So I see you chose: {game_options[player_decision]}!")

    # Make the computer choose its option
    computer_choice = game_options[random.randint(0, 2)]
    print(f"The computer chose: {computer_choice}!")

    # Decide who wins
    # 0 beats 2
    # 1 beats 0
    # 2 beats 1

    if player_choice == rock:
        if computer_choice == paper:
            print("\nYou lose!")
        elif computer_choice == rock:
            print("\nYou tied!")
        else:
            print("You won!")
    elif player_choice == scissors:
        if computer_choice == rock:
            print("\nYou lose!")
        elif computer_choice == scissors:
            print("\nYou tied!")
        else:
            print("You won!")
    elif player_choice == paper:
        if computer_choice == scissors:
            print("\nYou lose!")
        elif computer_choice == paper:
            print("\nYou tied!")
        else:
            print("You won!")