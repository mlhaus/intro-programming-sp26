"""
This module contains functions for getting user input from the keyboard
"""

import math
from datetime import datetime, date
from ui_helpers import show_message, show_error

def get_choice(options : list) -> int:
    """
    This function prompts the user for a choice
    Inputs: options, a list of strings
    Output: The value entered by the user
    """
    pass

def get_float(prompt: str, required = True, min = -math.inf, max = math.inf) -> float:
    """
    This function prompts the user for a decimal (float) number
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
        min - the lowest accepted value
        max - the highest accepted value
    Output: The value entered by the user
    """
    value = math.inf # if math.inf is returned, that indicates no value was entered.
    # were the min or max values changed?
    min_set = min != -math.inf
    max_set = max != math.inf
    while(True):
        print("\n" + prompt, end="") # Prints a blank line followed the prompt
        print(" (*)" if required else "", end="") # Prints an asterisk if the input is required
        if(min_set):
            print(f" [min {min}", end="") # Display min value in the prompt
        if(max_set):
            print(f"-max {max}]", end="") # Display max value in the prompt
        if(min_set and not max_set):
            print("]", end="")
        print(": ", end="") # Prints a separator between the prompt and the user's input
        try:
            value = float(input()) # Gets the value from user input
        except ValueError:
            if(not required):
                break # Allows the user to enter nothing if it's not required
            show_message("Invalid float value", "warning")
            continue # Restarts the loop if the value is required
        if(value < min):
            show_error("Value too low")
            continue # Restart the loop if the value entered is too low
        if(value > max):
            show_error("Value too high")
            continue # Restart the loop if the value entered is too high
        break # Ends the loop if a valid value is entered
    return value
        
def get_int(prompt: str, required = True, min = -math.inf, max = math.inf) -> int:
    """
    This function prompts the user for a whole (int) number
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
        min - the lowest accepted value
        max - the highest accepted value
    Output: The value entered by the user
    """
    value = math.inf
    min_set = min != -math.inf
    max_set = max != math.inf
    while(True):
        print("\n" + prompt, end="")
        print(" (*)" if required else "", end="")
        if(min_set):
            print(f" [min {min}", end="")
        if(max_set):
            print(f"-max {max}]", end="")
        if(min_set and not max_set):
            print("]", end="")
        print(": ", end="")
        try:
            value = int(input())
        except ValueError:
            if(not required):
                break
            show_error("Invalid integer value")
            continue
        if(value < min):
            show_error("Value too low")
            continue
        if(value > max):
            show_error("Value too high") 
            continue 
        break
    return value

def get_str(prompt: str, required = True) -> str:
    """
    This function prompts the user for a string
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    while(True):
        print("\n" + prompt, end="")
        print(" (*)" if required else "", end="")
        print(": ", end="")
        value = input()
        if(value == "" and not required):
            value = None
            break
        elif(value == "" and required):
            print("Value is required")
            continue
        break
    return value

def get_date(prompt: str, required = True, min = date.min, max = date.max) -> datetime:
    """
    This function prompts the user for date
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
        min - the lowest accepted value
        max - the highest accepted value
    Output: The value entered by the user
    """
    min_set = min != date.min
    max_set = max != date.max
    while(True):
        print("\n" + prompt, end="")
        print(" (*)" if required else "", end="")
        print(" [YYYY-MM-DD]", end="")
        if(min_set):
            print(f" [min {min}", end="")
        if(max_set):
            print(f"-max {max}]", end="")
        if(min_set and not max_set):
            print("]", end="")
        print(": ", end="")
        try:
            value = datetime.strptime(input(), "%Y-%m-%d")
        except ValueError:
            if(not required):
                value = None
                break
            show_error("Invalid date value")
            continue
        value = value.date() # Convert the datetime to date
        if(value < min):
            show_error("Value too low")
            continue
        if(value > max):
            show_error("Value too high") 
            continue 
        break
    return value

def get_bool(prompt: str, required = True) -> bool:
    """
    This function prompts the user for a Yes or No question
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
    Output: The value entered by the user (yes = True, no = False)
    """
    pass

def main():
    # print(get_float("Enter your height in inches", min = 0)) # Prompt for a required non-negative value
    # print(get_float("Enter your GPA", min = 0, max = 4)) # Prompt for a required value within a range
    # print(get_float("What is the current temperature?", False)) # Prompt for an optional value
    # print(get_float("What is your salary?")) # Prompt for a required value, any number is acceptable.
    # print(get_int("What is your favorite number?"))
    # print(get_int("What is your favorite number?", False))
    # print(get_int("What is your age?", True, 0))
    # print(get_int("Guess a number between 1 and 10", True, 1, 10))
    # print(get_str("What is your name?"))
    # print(get_str("What is your name?", False))
    # print(get_date("What is your birthday?"))
    print(get_date("What is your birthday?", False))
    print(get_date("What is your birthday?", True, date(1970, 1, 1)))
    print(get_date("What is your birthday?", True, date(1970, 1, 1), date.today()))

if __name__ == "__main__":
    main()