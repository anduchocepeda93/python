from students import Student

""" student1 = Student("John Doe", 20, "S12345", "Computer Science", 3.8, False)

print(student1)
print(student1.name)  # Output: John Doe
print(student1.age)  # Output: 20
print(student1.student_id)  # Output: S12345
print(student1.major)  # Output: Computer Science
print(student1.gpa)  # Output: 3.8
print(student1.is_on_probation)  # Output: False""" 

student2 = Student(input("Enter name: "), int(input("Enter age: ")), input("Enter student ID: "), input("Enter major: "), float(input("Enter GPA: ")), input("Is the student on probation? (yes/no): ").lower() == 'yes')

print(f"Student's name: {student2.name}")
print(f"Student's age: {student2.age}")
print(f"Student's ID: {student2.student_id}")
print(f"Student's major: {student2.major}")
print(f"Student's GPA: {student2.gpa}")
print(f"Student is on probation: {student2.is_on_probation}")