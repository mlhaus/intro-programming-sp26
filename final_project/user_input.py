"""
This module contains functions for getting user input from the keyboard
"""

import math
from datetime import datetime
from ui_helpers import show_message

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
    while(True):
        print("\n" + prompt, end="") # Prints a blank line followed the prompt
        print(" (*)" if required else "", end="") # Prints an asterisk if the input is required
        print(": ", end="") # Prints a separator between the prompt and the user's input
        try:
            value = float(input()) # Gets the value from user input
        except ValueError:
            if(not required):
                break # Allows the user to enter nothing if it's not required
            show_message("Invalid float value", "warning")
            continue # Restarts the loop if the value is required
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
    pass

def get_str(prompt: str, required = True) -> str:
    """
    This function prompts the user for a string
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
    Output: The value entered by the user
    """
    pass

def get_date(prompt: str, required = True, min = datetime.min, max = datetime.max) -> datetime:
    """
    This function prompts the user for date
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
        min - the lowest accepted value
        max - the highest accepted value
    Output: The value entered by the user
    """
    pass

def get_bool(prompt: str, required = True) -> bool:
    """
    This function prompts the user for a Yes or No question
    Inputs: prompt (required) - a text string asking the user a question,
        required - a boolean determining if input is required
    Output: The value entered by the user (yes = True, no = False)
    """
    pass

def main():
    print(get_float("What is the current temperature?", False))
    print(get_float("What is your salary?"))

if __name__ == "__main__":
    main()