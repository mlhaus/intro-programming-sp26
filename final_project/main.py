import ui_helpers as ui
import employee_handlers as eh
from user_input import get_int
'''
This is the main module for the Employee demo project
'''
def main():
    """
    Description: Displays a menu in a loop, responding to the user's inputs until the user chooses to quit
    Input: none
    Output: none
    """
    ui.show_program_title("Employee Management Program")
    while(True):
        choice = get_int("Choice", True, 1, 6)
        if(choice == 1):
            eh.add_employee()
        elif(choice == 2):
            eh.get_employee()
        elif(choice == 3):
            eh.get_all_employees()
        elif(choice == 4):
            eh.update_employee()
        elif(choice == 5):
            eh.delete_employee()
        elif(choice == 6):
            # To do: implement the confirm_quit functionality
            ui.confirm_quit()
            break
        ui.press_enter_to_continue()
    ui.show_message("Program complete. Have a great day.")


if __name__ == "__main__":
    main()