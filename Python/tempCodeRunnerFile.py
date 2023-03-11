# https://www.youtube.com/watch?v=eWRfhZUzrAc&list=PLIyH1NEzrU5j9LB4zFv-c7SU0UMd4vp4z&index=1&ab_channel=freeCodeCamp.org

# Imports a list of instrucitons into our program.
import random # This module implements pseudo-random number generators for various distributions.
              
# Variables and functions.
def get_choices(): # Created function "get_choices" and assigned variable.
    player_choice = input("Enter a choice, rock, paper or scissors ") # Created input variable "player_Choice" and assigning the users input (\n creates a new line in the console).
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options) # Created variable "computer_choice" and assigned a random string from "options".
    choices = {"player": player_choice, "computer": computer_choice} # Ceating a variable with a dictionary of {key: value, key: value}.

choices = get_choices()
print(choices)