# Create a dictionary employee_dict with the following key-value pairs: "John" : {"salary" : 5000, "department" : "Sales"}, "Mike" : {"salary" : 6000, "department" : "Marketing"}, "Sara" : {"salary" : 7000, "department" : "Operations"}.
# Write a program to find the employee with the highest salary in employee_dict.
# Write a program to find the average salary of all employees in employee_dict.
# Write a program to add a new employee to employee_dict.
# Write a program to remove an employee from employee_dict.
# Here We Use Nested Dictionary:-

employee_dict = {
    "John" : {"salary" : 5000, "department" : "Sales"},
    "Mike" : {"salary" : 6000, "department" : "Marketing"},
    "Sara" : {"salary" : 7000, "department" : "Operations"}
}

# Find the highest Salary among all these salary:-
salary = []
max_salary = employee_dict["John"]["salary"]
for i in employee_dict.values():
    if i["salary"] > max_salary:
        max_salary = i["salary"]
    salary.append(i["salary"])

# Find the employee name with the highest Salary:-
for name, values in employee_dict.items():
    if values["salary"] == max_salary:
        print("Person with highest paid:", name)

# Find the average salary of all employee in  employee_dict :-
total = sum(salary)
print("The average salary of all employee:",total/len(salary))

