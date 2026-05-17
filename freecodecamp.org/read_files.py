

#employee_file = open("employees.txt", "w")
#employee_file = open("employees.txt", "r")
employee_file = open("employees.txt", "r+")
print(employee_file.readable())
print(employee_file.writable())
print(employee_file.readline())
print(employee_file.readlines()[0])
#print(employee_file.write("Kelly - Customer Service\n"))
#print(employee_file.read())

for employee in employee_file.readlines():
    print(employee)
    
employee_file.close()
