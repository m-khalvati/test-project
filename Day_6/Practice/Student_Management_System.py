import platform
import subprocess
import time

import add_student
import remove_student
import search_student


# Function to clear the console screen based on different operating systems
def clear_screen():
    system = platform.system()
    if system == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


# Initial list of students
students = [
    {"name": "Morteza", "age": 27},
    {"name": "Reza", "age": 19},
    {"name": "Sara", "age": 22},
]


def main_menu():
    while True:
        clear_screen()
        print("==============================")
        print("   Student Management System  ")
        print("==============================")
        print("1. Show Students")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. Count Students")
        print("5. Search Student")
        print("0. Exit")
        print("==============================")

        choice = input("Select an option: ")

        match choice:
            case "1":
                # print the list of students
                clear_screen()
                print("=== List of Students ===\n")
                for student in students:
                    print(student)
                input("\nPress Enter to return to the menu...")
            case "2":
                # add a new student
                clear_screen()
                student = add_student.add()
                students.append(student)
                print(f"student {student['name']} added successfully!")
                # delay for see the result's
                time.sleep(1.5)
            case "3":
                # remove a student by name
                clear_screen()
                student = remove_student.remove(students)
                if student:
                    students.remove(student)
                    print(f"Student {student['name']} removed successfully!")
                time.sleep(2)
            case "4":
                # Count the number of students
                clear_screen()
                print("=== Count Students ===")
                print(f"Total number of students: {len(students)}")
                input("\nPress Enter to return to the menu...")
            case "5":
                # Search for a student by name
                clear_screen()
                student = search_student.search(students)
                if student:
                    print(f"Student found: {student}")
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
