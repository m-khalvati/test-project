def search(students):
    print("=== Search Student ===")
    name = input("Enter the name of the student to search: ")

    for student in students:
        if student["name"] == name:
            return student

    print(f"No student found with the name {name}.")
