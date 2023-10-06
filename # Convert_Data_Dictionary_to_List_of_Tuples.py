# Convert Data Dictionary to List of Tuples:-

data_dict = {'Company Name': ['Wipro', 'Deloitte', 'HP'],
             'Employee Type': ['Developer', 'Data Engineer', 'Data Scientist']}

company_names = data_dict['Company Name']                 # ['Wipro', 'Deloitte', 'HP']

employee_types = data_dict['Employee Type']               # ['Developer', 'Data Engineer', 'Data Scientist']

len_of_dict = len(company_names)                          # 3

data_in_tuples = []

for i in range(len_of_dict):
    company_name = company_names[i]
    employee_type = employee_types[i]
    data_in_tuples.append((company_name, employee_type))
print(data_in_tuples)
