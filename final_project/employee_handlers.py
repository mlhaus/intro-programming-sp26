from ui_helpers import press_enter_to_continue, show_message
from user_input import get_float, get_int, get_date, get_bool, get_str
from table import print_table
import copy
from employee_data import update_data, get_data, add_data, get_employee_list, get_needed_fields, get_employees_by_name
'''
This module contains functions related to creating, reading, updating, and deleting employee records
'''

# employees = []
# employees_headings = ["Name", "Date of Birth", "# Dependents",  "Extra withholding", "Tax exempt?"]

def add_employee():
    """
    Handles logic for adding one employee record
    INPUTS: None
    OUTPUT: None
    """
    # prompt user for employee data
    employee_data = get_employee_data()
    # Print the list of employees
    add_data(employee_data)

def get_employee_data():
    """
    Prompt the user for the employee's name (first, last), dob, dependents, extra withholding
    INPUTS: employee, a optional list containing employee data
    OUTPUT: None
    """
    employee = []
    employees_headings = get_needed_fields()
    employee.append(get_str(employees_headings[0])) # Name
    employee.append(get_date(employees_headings[1])) # DOB
    employee.append(get_int(employees_headings[2], min=0, max=10)) # Dependents
    employee.append(get_float(employees_headings[3], min=0)) # Extra Withholding
    employee.append(get_bool(employees_headings[4])) # Tax exempt
    return employee


def get_all_employees():
    """
    Handles logic for displaying all employee records
    INPUTS: None
    OUTPUT: None
    """
    employees_copy =  sorted(get_employee_list(), key=lambda x: x[0]) # Sort alphabetically by name
    employees_copy.insert(0, get_needed_fields())
    print_table(employees_copy)

def get_employee():
    """
    Handles logic for getting one employee record
    INPUTS: None
    OUTPUT: None
    """
    name_to_search = get_str("Enter the employee's name")
    employees = get_employees_by_name(name_to_search)
    if(employees == None):
        show_message("No employee records found", "error")
    else:
        copy_employees = sorted(employees, key=lambda x: x[0])
        copy_employees.insert(0, get_needed_fields())
        print_table(copy_employees)
    return employees


def update_employee():
    """
    Handles logic for updating one employee record
    INPUTS: None
    OUTPUT: None
    """
    # employee_list is a multi-dimensional list
    employee_list = get_employee()
    if(employee_list == None):
        return # No employee records found, so return to the main menu
    elif(len(employee_list) > 1):    
        show_message("Multiple employees found. Please be more specific.", "error")
    else:
        single_employee = employee_list[0]
        # Implement update logic for a single employee
        show_message("Press enter to keep the existing value")
        # Don't prompt the user to change the 'unique' identifying field
        # In this example, it will be the employee's name
        # In a better example, it would be the employee's id or ssn
        employees_headings = get_needed_fields()
        date_of_birth = single_employee[1] # current date of birth
        new_date_of_birth = get_date(f"{employees_headings[1]} ({date_of_birth})", False) # DOB
        if(new_date_of_birth != None):
            single_employee[1] = new_date_of_birth.strftime("%Y-%m-%d")
        
        
        
        
        # employee_list[2] = get_int(employees_headings[2], min=0, max=10) # Dependents
        # num_dependents = employee_list[2] # int
        # employee_list[3] = get_float(employees_headings[3], min=0) # Extra Withholding
        # extra_withholding = employee_list[3] # float
        # employee_list[4] = get_bool(employees_headings[4])# Tax exempt
        # is_tax_exempt = employee_list[4] # bool

        update_data(single_employee)


def delete_employee():
    """
    Handles logic for deleting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def main():
    # To do: call get_all_employees()
    pass

if __name__ == "__main__":
    main()