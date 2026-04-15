'''
The functions in this module will help us define User Interface appearance
'''

CONSOLE_WIDTH = 80

def show_message(message: str, type = "") -> None:
    """
    Displays a message
    INPUTS:
        message, A string with the text to display
        type, A string such as "error", "title", etc.
    OUTPUT: None
    """
    print("\n" + (type.upper() + ": " if(type != "") else "") + message)

def show_program_title(title: str) -> None:
    """
    Displays the formatted program title
    INPUT: title, A string with the title of the program
    OUTPUT: None
    """
    show_message(f'\n{"** " + title + " **":^{CONSOLE_WIDTH}}')

def show_menu(menu_title: str, options: list) -> None:
    """
    Displays the menu title and then displays the menu options, one per line
    INPUTS:
        menu_title, A string with the name of the menu
        options, A list of strings with the options for the menu
    OUTPUT: None
    """
    pass

def show_section_title(title: str) -> None:
    """
    Displays a section title
    INPUT: title, A string with title of the section
    OUTPUT: None
    """
    show_message(f'{"-- " + title + " --":^{CONSOLE_WIDTH}}')

def show_error(message: str) -> None:
    """
    Displays an error message and then requests that the user press Enter to continue
    INPUTS: message, A string with the error message
    OUTPUT: None
    """
    show_message(message, "error")
    press_enter_to_continue()

def press_enter_to_continue() -> None:
    """
    Displays a message instructing the user to press  the Enter key and then waits until they do
    INPUT: None
    OUTPUT: None
    """
    input("Press Enter to continue...")

def confirm_quit() -> bool:
    """ 
    Displays a message stating that the user has chosen to quit. Then asks the user to confirm the desire 
    to quit by entering Y
    INPUT: None
    RETURNS: boolean True if the user confirms the quit, and False otherwise
    """
    from user_input import get_bool
    return get_bool("Are you sure you want to quit?")

def main():
    # press_enter_to_continue()
    # show_message("Number cannot be negative", "error")
    # show_message("You have entered 10 employees", "warning")
    # show_message("New employee created", "success")
    # show_message("It's a great day to be alive!")
    # show_error("Number cannot be negative")
    show_program_title("Employee Management Program")
    show_section_title("Add a new employee")

if __name__ == "__main__":
    main()

'''
confirm_quit import explanation:

The error you were getting (`ImportError: cannot import name 'show_message' from 'ui_helpers'`) was caused by a **circular import**. 

Here was what was happening:
1. `main.py` imports `show_message` from `ui_helpers.py`
2. `ui_helpers.py` starts loading and imports `get_bool` from `user_input.py`
3. `user_input.py` starts loading and imports `show_message` and `show_error` from `ui_helpers.py`
4. Since `ui_helpers.py` hasn't finished loading yet (it paused to load `user_input.py`), its functions aren't ready to be imported yet! When `user_input.py` tries to import `show_message`, Python throws the `ImportError`.

### How I solved it
In Python, one of the easiest ways to handle circular imports is to delay the import until it's actually needed. Since `get_bool` was only being used by the `confirm_quit()` function in `ui_helpers.py`, I moved the `from user_input import get_bool` statement from the top of the file into the `confirm_quit()` function itself. 

I've made the modifications and the background command I ran confirms the program now runs without errors and displays the `--- MAIN MENU ---` properly. You should be good to go!
'''