#!/usr/bin/env python3

# This file represents the end of day project 
# presented in day 3 of the Udemy Course for 100 Days of Python

# Treasure Island Project
print(''')
                   `\-.   `
                      \ `.  `
                       \  \ |
              __.._    |   \.       S O N - G O K U
       ..---~~     ~ . |    Y
         ~-.          `|    |
            `.               `~~--.
              \                    ~.
               \                     \__. . -- -  .
         .-~~~~~      ,    ,            ~~~~~~---...._
      .-~___        ,'/  ,'/ ,'\          __...---~~~
            ~-.    /._\_( ,(/_. 7,-.    ~~---...__
           _...>-  P""6=`_/"6"~   6)    ___...--~~~
            ~~--._ \`--') `---'   9'  _..--~~~
                  ~\ ~~/_  ~~~   /`-.--~~
                    `.  ---    .'   \_
                      `. " _.-'     | ~-.,-------._
                  ..._../~~   ./       .-'    .-~~~-.
            ,--~~~ ,'...\` _./.----~~.'/    /'       `-
        _.-(      |\    `/~ _____..-' /    /      _.-~~`.
       /   |     /. ^---~~~~       ' /    /     ,'  ~.   \
      (    /    (  .           _ ' /'    /    ,/      \   )
      (`. |     `\   - - - - ~   /'      (   /         .  |
       \.\|       \            /'        \  |`.           /
       /.'\\      `\         /'           ~-\         .  /\
      /,   (        `\     /'                `.___..-      \
     | |    \         `\_/'                  //      \.     |
     | |     |                 ______      /' |       |     |
''')
# Welcome player
print("Welcome to to Z City!")
print("Let's find the dragon balls!")

# Ask first choice, instantiate others
choice_one = input("Left or right?\n").lower()
choice_two = ""
choice_three = ""

# If left -> keep going
# If right or anything else, you lose
if choice_one == "left":
    # Second question
    # If wait -> keep going
    # If swim or anything else, you lose
    choice_two = input("You found a lake! Swim in or wait on the shore?\n").lower()
    if choice_two == "wait":
        # Third question
        # If red -> burned by Shenron, you lose
        # If blue -> whooped by Frieza, you lose
        # If yellow -> you win
        choice_three = input("Two doors appeared! Walk through the red or blue one?\n").lower()
        if choice_three == "yellow":
            print("You found the dragonballs!")
        elif choice_three == "blue":
            print("You were EATEN? HOW did you manage that??")
        elif choice_three == "red":
            print("You got hit with a NASTY kamehameha")
        else:
            print("That wasn't even an option. You lose.")
    else:
        print("You tried the water and were eaten alive! GG's!")
# You lose off rip
else:
    print("You fell into a hole looking for them! Maybe next time!")

