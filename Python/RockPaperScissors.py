# https://www.youtube.com/watch?v=eWRfhZUzrAc&list=PLIyH1NEzrU5j9LB4zFv-c7SU0UMd4vp4z&index=1&ab_channel=freeCodeCamp.org

# variables and functions

def get_choices(): # created function "get_choices" and assigned variable
    player_choice = input("Enter a choice, rock, paper or scissors \n") # created input variable "player_Choice" and assigning the users input (\n creates a new line in the console)
    computer_choice = "paper" # created variable "computer_choice" and assigned "paper"
    choices = {"player": player_choice, "computer": computer_choice} # ceating a variable with a dictionary of {key: value, key: value}

    return choices # when the "get_choices" funstion is called the "choices" dictionary is returned

get_choices()