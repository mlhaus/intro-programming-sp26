# Define all the hard-coded strings.
program_title = "*** Employee Program ***"
employee_id_prompt = "Please enter the employee ID: "
last_name_prompt = "Please enter the employee last name: "
first_name_prompt = "Please enter the employee first name: "
department_prompt = "Please enter the department name: "
salary_prompt = "Please enter the employee annual salary: "
table_name = "Employee Data"
id_header = "ID"
emp_name_header = "EMPLOYEE NAME"
dept_header = "DEPARTMENT"
salary_header = "SALARY"
col1_width = 5
col2_width = 20
col3_width = 15
col4_width = 12
num_columns = 4
table_width = col1_width + col2_width + col3_width + col4_width + (num_columns * 3 + 1)
program_complete = "Program complete."

print(f"{program_title}")
# Prompt the user for input
employee_id = int(input(employee_id_prompt))
last_name = input(last_name_prompt)
first_name = input(first_name_prompt)
department = input(department_prompt)
salary = float(input(salary_prompt))
full_name = last_name + ', ' + first_name

# Display output
print(f'\n{table_name:^{table_width}s}')
print("-" * table_width)
print(f'| {id_header:^{col1_width}s} | {emp_name_header:^{col2_width}s} | {dept_header:^{col3_width}s} | {salary_header:^{col4_width}s} |')
print("-" * table_width)
print(f'| {employee_id:>{col1_width}d} | {full_name:<{col2_width}s} | {department:<{col3_width}s} | {salary:>{col4_width},.2f} |')
print("-" * table_width)

print(f'\n{program_complete}\n')