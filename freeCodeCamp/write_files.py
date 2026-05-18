
employee_file = open("employees.txt", "a")
#employee_file = open("employees.txt", "w")
#print(employee_file.writable())
print(employee_file.write("\nKelly - Customer Service"))

employee_file.close()


employee_file = open("employees_new.txt", "w")
print(employee_file.write("Kelly - Customer Service"))

employee_file.close()

