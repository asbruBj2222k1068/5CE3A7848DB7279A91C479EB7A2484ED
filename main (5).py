class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example student objects
student1 = Student("Alice", "101", 3.8)
student2 = Student("Bob", "102", 3.5)
student3 = Student("Charlie", "103", 3.9)

student_list = [student1, student2, student3]

sorted_student_list = sort_students(student_list)

for student in sorted_student_list:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")