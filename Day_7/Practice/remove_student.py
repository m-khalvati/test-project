def remove(students):
    print("=== Remove Student ===")
    if not students:
        print("No students available to remove.")
        return None

    print("Current list of students:\n")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']}")
    print("------------------------")

    # check input for valid integer ID
    try:
        student_id = int(input("\nEnter the ID of the student to remove: "))
    except ValueError:
        print("\nInvalid ID format! ID must be an integer.")
        return None

    for student in students:
        if student["id"] == student_id:
            return student

    print(f"\nNo student found with ID: {student_id}")
    return None
