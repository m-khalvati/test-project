class Student:
    def __init__(self, student_id, first_name, last_name, gpa, age):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.age = age

    # Display student details
    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"GPA: {self.gpa}")
        print(f"Age: {self.age}")
        print("-------------------------")

    # Add student to list
    @staticmethod
    def add_student(student_list, student):
        student_list.append(student)
        print(f"Student '{student.first_name}' added successfully!")

    # Remove student by ID
    @staticmethod
    def remove_student(student_list, student_id):
        for student in student_list:
            if student.student_id == student_id:
                student_list.remove(student)
                print(f"Student with ID {student_id} removed successfully!")
                return True
        print(f"Student with ID {student_id} not found!")
        return False