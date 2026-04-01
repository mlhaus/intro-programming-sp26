from ui_helpers import press_enter_to_continue, show_message
from user_input import get_float, get_int, get_date, get_bool, get_str
from table import print_table
import copy
'''
This module contains functions related to creating, reading, updating, and deleting employee records
'''

employees = []
employees_headings = ["Name", "DOB", "# Dependents",  "Extra withholding", "Tax exempt?"]

def add_employee():
    """
    Handles logic for adding one employee record
    INPUTS: None
    OUTPUT: None
    """
    # prompt the user for new employee data
    get_employee_data()
    # Print the list of employees
    get_all_employees()

def get_employee_data():
    """
    Prompt the user for the employee's name (first, last), dob, dependents, extra withholding
    INPUTS: employee, a optional list containing employee data
    OUTPUT: None
    """
    employee = []
    employee.append(get_str(employees_headings[0])) # Name
    employee.append(get_date(employees_headings[1])) # DOB
    employee.append(get_int(employees_headings[2], min=0, max=10)) # Dependents
    employee.append(get_float(employees_headings[3], min=0)) # Extra Withholding
    employee.append(get_bool(employees_headings[4])) # Tax exempt
    employees.append(employee)
    show_message("Employee added", "success")


def get_all_employees():
    """
    Handles logic for displaying all employee records
    INPUTS: None
    OUTPUT: None
    """
    employees_copy = copy.deepcopy(employees)
    employees_copy.insert(0, employees_headings)
    print_table(employees_copy)
    press_enter_to_continue()

def get_employee():
    """
    Handles logic for getting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def update_employee():
    """
    Handles logic for updating one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def delete_employee():
    """
    Handles logic for deleting one employee record
    INPUTS: None
    OUTPUT: None
    """
    pass

def main():
    pass

if __name__ == "__main__":
    main()