def search(students):
    print("=== Search Student ===")
    if not students:
        print("No students in the database.")
        return []

    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Select search method (1/2): ").strip()

    found_students = []

    # found student by ID
    if choice == "1":
        try:
            student_id = int(input("\nEnter the ID of the student to search: "))
        except ValueError:
            print("\nInvalid ID format! ID must be an integer.")
            return []

        for student in students:
            if student["id"] == student_id:
                found_students.append(student)
                break

        if not found_students:
            print(f"\nNo student found with ID: {student_id}")

    # found student by Name
    elif choice == "2":
        name = input("\nEnter the name of the student to search: ").strip().lower()
        if not name:
            print("Name cannot be empty.")
            return []

        # Search all students with same name
        for student in students:
            if student["name"].lower() == name:
                found_students.append(student)

        if not found_students:
            print(f"\nNo student found with Name: '{name}'")

    else:
        print("\nInvalid option selected!")

    return found_students
