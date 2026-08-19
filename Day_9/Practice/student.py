import os


class BaseEntity:

    def __init__(self, item_id, filename):
        self.item_id = item_id
        self.filename = filename


# Inheriting BaseEntity
class Student(BaseEntity):

    def __init__(self, student_id, first_name, last_name, gpa, age):
        super().__init__(student_id, "students.txt")
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.age = age

    # Format student data : CSV string
    def to_csv(self):
        return (
            f"{self.item_id},{self.first_name},{self.last_name},{self.gpa},{self.age}\n"
        )

    # Save student
    def save_to_file(self):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(self.to_csv())
        print(f"Student '{self.first_name}' added to file successfully!")

    # Display all students
    @classmethod
    def display_all(cls, filename="students.txt"):
        if not os.path.exists(filename):
            print("No students record found.")
            return

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No students found in file.")
                return

            print("=== Students List ===")
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    print(f"ID: {parts[0]}")
                    print(f"Name: {parts[1]} {parts[2]}")
                    print(f"GPA: {parts[3]}")
                    print(f"Age: {parts[4]}")
                    print("-------------------------")

    # Remove student by ID
    @classmethod
    def remove_from_file(cls, student_id, filename="students.txt"):
        if not os.path.exists(filename):
            print("File not found!")
            return False

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts and int(parts[0]) == student_id:
                    found = True
                else:
                    file.write(line)

        if found:
            print(f"Student with ID {student_id} removed successfully!")
            return True
        else:
            print(f"Student with ID {student_id} not found!")
            return False
