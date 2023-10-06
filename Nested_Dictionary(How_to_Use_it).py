# Here We Use Nested Dictionary:-

employee_dict = {
    "John": {"salary": 5000, "department": "Sales"},
    "Mike": {"salary": 6000, "department": "Marketing"},
    "Sara": {"salary": 7000, "department": "Operations"}
}
emp = {}
for i in range(0, 3):
    name = input("Enter the name:")
    salary = int(input("Enter the salary:"))
    department = input("Enter the department:")

    emp[name] = dict([("salary", salary), ("department", department)])
print(emp)




