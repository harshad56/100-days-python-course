class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        print("List of students:")
        for student in self.students:
            print(
                f"Name: {student.name}\tRoll Number: {student.roll_number}\tGrade: {student.grade}")


# Create an instance of the StudentManagementSystem
sms = StudentManagementSystem()

# Add students
sms.add_student("John Doe", "001", "A")
sms.add_student("Jane Smith", "002", "B")

# Display all students
sms.display_students()

# Remove a student
sms.remove_student("001")

# Display students after removal
sms.display_students()
