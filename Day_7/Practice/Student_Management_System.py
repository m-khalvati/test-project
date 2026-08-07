import os
import platform
import subprocess
import time

import add_student
import remove_student
import search_student

# File path
DATA_FILE = "students_data.txt"


# Load students
def load_students():
    students = []
    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            # Ignore empty lines
            if line:
                parts = line.split(",")
                if len(parts) == 3:
                    student_id = int(parts[0])
                    name = parts[1]
                    age = int(parts[2])
                    students.append({"id": student_id, "name": name, "age": age})
    return students


# Save students
def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student['id']},{student['name']},{student['age']}\n")


# Function to clear the console screen
def clear_screen():
    system = platform.system()
    if system == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def main_menu():
    # Load initial data
    students = load_students()

    while True:
        clear_screen()
        print("==============================")
        print("   Student Management System  ")
        print("==============================")
        print("1. Show Students")
        print("2. Add Student")
        print("3. Remove Student by ID")
        print("4. Count Students")
        print("5. Search Student by ID")
        print("0. Exit")
        print("==============================")

        choice = input("Select an option: ")

        match choice:
            case "1":
                # print the list of students
                clear_screen()
                print("=== List of Students ===\n")
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(f"ID: {student['id']}")
                        print(f"Name: {student['name']}")
                        print(f"Age: {student['age']}")
                        print("------------------------")
                input("\nPress Enter to return to the menu...")

            case "2":
                # add a new student
                clear_screen()
                student = add_student.add(students)
                students.append(student)
                # Save changes in file
                save_students(students)
                print(
                    f"\nStudent '{student['name']}' (ID: {student['id']}) added successfully!"
                )
                time.sleep(1.5)

            case "3":
                # remove a student by name or ID
                clear_screen()
                student = remove_student.remove(students)
                if student:
                    students.remove(student)
                    # Save changes in file
                    save_students(students)
                    print(
                        f"\nStudent '{student['name']}' (ID: {student['id']}) removed successfully!"
                    )
                time.sleep(2)

            case "4":
                # Count the number of students
                clear_screen()
                print("=== Count Students ===")
                print(f"Total number of students: {len(students)}")
                input("\nPress Enter to return to the menu...")

            case "5":
                # Search for a student by ID or Name
                clear_screen()
                found_students = search_student.search(students)
                if found_students:
                    print(f"\n=== Found {len(found_students)} Student(s) ===")
                    for student in found_students:
                        print(f"ID: {student['id']}")
                        print(f"Name: {student['name']}")
                        print(f"Age: {student['age']}")
                        print("------------------------")
                input("\nPress Enter to return to the menu...")

            case "0":
                print("\nClosing the program. Goodbye!")
                break

            case _:
                print("\n[ERROR] Invalid option! Please try again.")
                time.sleep(1)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting...")
