'''
Hello World
FILE:	lab4.py
DATE:	2026-02-11
AUTHOR: Marc Hauschildt
DESCRIPTION:
	This is the start of a menu-driven program that allows a 
    Human Resources (HR) clerk to manage employee data records.
'''

# Define all the hard-coded strings.
program_title = "*** Employee Program ***"
main_menu_title = "-- Main Menu --"
add_employee = "Add an Employee"
show_all_employees = "Show All Employees"
view_employee = "View an Employee"
update_employee = "Update an Employee"
delete_employee = "Delete an Employee"
quit = "Quit"
menu_prompt = "Your choice: "
choice_response = "You chose to"
error_response = "Your choice was not recognized.  Please try again."
press_enter = "Press the Enter key to continue..."
program_complete = "Program complete."
console_width = 80

# Greet the user
print(f"\n{program_title:^{console_width}s}")

# Prompt the user for input
print(f"{main_menu_title:^{console_width}s}")
print(f"1.\t{add_employee}")
print(f"2.\t{show_all_employees}")
print(f"3.\t{view_employee}")
print(f"4.\t{update_employee}")
print(f"5.\t{delete_employee}")
print(f"6.\t{quit}")

print(f"\n{menu_prompt}", end="")
choice = int(input())

# Display output
if(choice == 1):
    print(f"{choice_response} {add_employee.lower()}")
elif(choice == 2):
    print(f"{choice_response} {show_all_employees.lower()}")
elif(choice == 3):
    print(f"{choice_response} {view_employee.lower()}")
elif(choice == 4):
    print(f"{choice_response} {update_employee.lower()}")
elif(choice == 5):
    print(f"{choice_response} {delete_employee.lower()}")
else:
    print(f"{choice_response} {quit.lower()}")

print(f"\n{press_enter}", end="")
input()
print(f"{program_complete}")