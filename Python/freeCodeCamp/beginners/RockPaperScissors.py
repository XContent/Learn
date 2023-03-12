# https://www.youtube.com/watch?v=eWRfhZUzrAc&list=PLIyH1NEzrU5j9LB4zFv-c7SU0UMd4vp4z&index=1&ab_channel=freeCodeCamp.org

# Imports a list of instrucitons into our program.
import random # This module implements pseudo-random number generators for various distributions.
              
# Variables and functions.
def get_choices(): # Created function "get_choices" and assigned variable.
    player_choice = input("Enter a choice, rock, paper or scissors ") # Created input variable "player_Choice" and assigning the users input (\n creates a new line in the console).
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options) # Created variable "computer_choice" and assigned a random string from "options".
    choices = {"player": player_choice, "computer": computer_choice} # Ceating a variable with a dictionary of {key: value, key: value}.

    return choices # When "get_choices" is called, the "return" function will output "choices".

# Function arguments.
def check_win(player, computer): # Created function "check_win" reuiring 2 pieces of data.
    # Contcatenating strings combining strings with variables.
    print(f"You chose {player}\nYour opponent chose {computer}") 
    # If statement will allow a program to execute different tasks under certain conditions.
    if player == computer: # Comparing values between the variables "player" and "computer".
        return "It's a tie" # If both "player" and "computer" chose the same option.
    elif player == "rock":
        if computer == "scissors": # Nested if statement.
            return "Rock beats scissors You win!"
        else:
            return "paper covers rock, you lose"
    elif player == computer:
        return "It's a tie"
    elif player == "paper":
        if computer == "rock":
            return "paper coveres rock, You win!"
        else:
            return "scissors cuts paper, you lose"
    elif player == computer:
        return "It's a tie"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper, you win!"
        else:
            return "Rock beats scissors, You lose"
    
    # Else and elif statements will allow a program to execute different tasks under certain conditions if it does not meet the previous if, elif, else statements requirments.
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)