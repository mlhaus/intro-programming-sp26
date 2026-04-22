from data_helpers import process_file, write_file
from ui_helpers import show_message, press_enter_to_continue
from datetime import datetime

FILE_NAME = "employees.csv"

def get_needed_fields():
    return ["Name", "Date of Birth", "# Dependents",  "Extra withholding", "Tax exempt?"]

def get_data() -> list:
    '''
    Returns an unformatted list of employees from a CSV file.
    '''
    return process_file(FILE_NAME, get_needed_fields())

def get_employee_list():
    '''
    Returns a formatted list of employees
    '''
    unformatted_employees = get_data()
    formatted_employees = []
    for employee in unformatted_employees:
        formatted_employee = []
        formatted_employee.append(employee[0]) # Append the name
        formatted_employee.append(datetime.strptime(employee[1], "%Y-%m-%d").date()) # Format and append the date
        formatted_employee.append(int(employee[2])) # Append number of dependents formatted as an int
        formatted_employee.append(float(employee[3])) # Append extra withholding formatted as a float
        # https://gemini.google.com/share/a53a8e7e2cd9
        formatted_employee.append(employee[4].capitalize() == "True") # Append exemption status formatted as a boolean
        formatted_employees.append(formatted_employee)
    return formatted_employees

def add_data(employee_data):
    '''
    Adds a new employee to the formatted list of employees
    '''
    employee_list = get_employee_list()
    employee_list.append(employee_data)
    write_file(FILE_NAME, get_needed_fields(), employee_list)
    show_message("Employee added", "success")
    
def get_employees_by_name(name: str) -> list:
    '''
    Input: name of employee
    Output: a list representing matched employees, or None if no one matches the name
    '''
    results = []
    for employee in get_employee_list():
        if name.lower() in employee[0].lower():
            results.append(employee)
    if(len(results) == 0):
        return None
    return results

def update_data(updated_employee: list):
    '''
    Inputs: a list containing data for a single employee record
    '''
    # employee_list is a multi-dimensional list 
    # where each inner list is an employee record. 
    employee_list = get_employee_list()
    # We loop through the employee_list one employee at a time.
    for i in range(len(employee_list)):
        # We check if the name of the employee matches the name of the updated_employee. 
        if employee_list[i][0] == updated_employee[0]: # If the name matches, update the record
            # If it does, we update that record with the new data
            employee_list[i] = updated_employee
            # And write the updated employee_list back to the file.
            write_file(FILE_NAME, get_needed_fields(), employee_list)
            show_message("Employee updated", "success")
            return



if __name__ == "__main__":
    print(get_employees_by_name("Marc Hauschildt"))
    print(get_employees_by_name("pig"))
    # print(get_data())
    # print(get_employee_list())
    # fake_employee = ["Jane Doe", "2026-04-13", 5, 100, False]
    # add_data(fake_employee)