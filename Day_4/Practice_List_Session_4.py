# List of student grades
grades = [18, 14, 12, 19, 15, 20, 11]

print("#### Passing Grades with Index ####")

# Using enumerate to get both index and grade
for index, grade in enumerate(grades):
    if grade > 15:
        print(f"Student at index {index} passed with grade: {grade}")