class Student:
    def __init__(self, name, age, student_id, major, gpa, is_on_probation):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation  
        
    def on_honor_roll(self):
        if self.gpa >= 3.5 and not self.is_on_probation:
            return True
        else:
            return False
    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Major: {self.major}, GPA: {self.gpa}, On Probation: {self.is_on_probation}" 
# Example usage:
student1 = Student("Alice", 20, "S001", "Computer Science", 3.8, False)
student2 = Student("Bob", 22, "S002", "Mathematics", 3.2, True)

print(student1)
print(student2)

print(f"{student1.name} is on honor roll: {student1.on_honor_roll()}")
print(f"{student2.name} is on honor roll: {student2.on_honor_roll()}")
