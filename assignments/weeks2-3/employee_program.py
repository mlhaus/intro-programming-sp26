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
col_width_1 = 20
col_width_2 = 20
col_width_3 = 20
col_width_4 = 20
program_complete = "Program complete."

print(f"{program_title}")
# Prompt the user for input
employee_id = int(input(employee_id_prompt))
last_name = input(last_name_prompt)
first_name = input(first_name_prompt)
department = input(department_prompt)
salary = float(input(salary_prompt))
full_name = last_name + ', ' + first_name
col_1_width = 20
col_2_width = 20
col_3_width = 20
col_4_width = 20

# Display output
print(f'\n{table_name}')

print(f'{id_header:^{col_1_width}s} | {emp_name_header:^{col_2_width}s} | {dept_header:^{col_3_width}s} | {salary_header:^{col_4_width}s}')
print(f'{employee_id:<{col_1_width}s} | {full_name:<{col_2_width}s} | {department:<{col_3_width}s} | {salary:>{col_4_width},2f}')

print(f'\n{program_complete}\n')