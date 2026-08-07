def add(students):
    print("=== Add Student ===\n")

    # Generate unique ID
    if students:
        new_id = max(student["id"] for student in students) + 1
    else:
        # Initial ID
        new_id = 1

    # Validation for non-empty name
    while True:
        name = input("Please enter the student's name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a valid name.\n")

    # Validation for age
    while True:
        try:
            age = int(input("Please enter the student's age: "))
            return {"id": new_id, "name": name, "age": age}
        except ValueError:
            print("\nInvalid input for age. Please enter a valid integer.\n")
