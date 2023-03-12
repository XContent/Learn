import random 

def greeting(): # Creating a function.
    return "Hi" # Returns a string with th value of "hi" (that on it's own will not output to console).

response = greeting() # Creating a variable "response" and assigning the value of the function "greeting".
print(response) # Outputs variable to console.

# Dictionaries - store data values in key data pairs.
dict = {"name": "beau", "colour": "blue"} # Ceating a variable with a dictionary of {key: value, key: value}.

# List is used to store multiple items in a single variable.
food = ["pizza", "carrots", "eggs"] # Creating a list "food" to store muliple items in a single variable.
dinner = random.choice(food) 

# If statement will allow a program to execute different tasks under certain conditions.
a = 3
b = 5
if a > b:
    print("yes")

# Contcatenating strings combining strings with variables.
jim_age = 25
print(f"Jim is {jim_age} years old")
user_age = "twentyfIve"
print("You are " + user_age + " years old")

# Else and elif statements will allow a program to execute different tasks under certain conditions if it does not meet the previous if, elif, else statements requirments.
# Else and elif statements will continue to cycle until statement is true and then it will run the code inside of the true statement.
age = 20
if age >= 18:
    print("you are an adult.")
elif age > 12:
    print("print you are a teenager.")
elif age > 1:
    print("your a child")
else:
    print("you are a baby")


# Accessing dictionaries.
choices = {"player": "rock", "computer": "paper"} # Ceating a variable with a dictionary of {key: value, key: value}.
player_choice = choices["player"] # Calling variable value from dictionary with get bracket [key] function.