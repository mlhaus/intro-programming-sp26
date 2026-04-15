from ui_helpers import show_program_title, show_section_title, show_message, confirm_quit
import employee_handlers as eh
from user_input import get_choice
'''
This is the main module for the Employee demo project
'''
def main():
    """
    Description: Displays a menu in a loop, responding to the user's inputs until the user chooses to quit
    Input: none
    Output: none
    """
    show_program_title("Employee Management Program")
    menu_options = ["Add an employee", "Get all employees", "Get employee(s) by name",
                    "Update an employee", "Delete an employee", "Quit"]
    while(True):
        print("\n--- MAIN MENU ---")
        choice = get_choice(menu_options)
        # Don't display the section title if the user chooses to quit
        if(1 <= choice < len(menu_options)):
            show_section_title(menu_options[choice - 1])
        if(choice == 1):
            eh.add_employee()
        elif(choice == 2):
            eh.get_all_employees()
        elif(choice == 3):
            eh.get_employee()
        elif(choice == 4):
            eh.update_employee()
        elif(choice == 5):
            eh.delete_employee()
        elif(choice == 6):
            if(confirm_quit()):
                break
        
        
    show_message("Program complete. Have a great day.")


if __name__ == "__main__":
    main()