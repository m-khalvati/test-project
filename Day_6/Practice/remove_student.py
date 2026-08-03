def remove(students):
    print("=== Remove Student ===")
    print("Current list of students:")

    for student in students:
        print(student)
    name = input("Enter the name of the student to remove: ")

    for student in students:
        if student["name"] == name:
            return student

    print(f"No student found with the name {name}.")
