key_list = ['Location', 'Salary']
employee_dict = {
    "Name": "Miguel", 
    "Last Name": "Gonzalez", 
    "Role": "CyberSecurity Engineer",
    "Location": "San Jose",
    "Salary": "100"
    }

for key in key_list:
    employee_dict.pop(key)
print(employee_dict)