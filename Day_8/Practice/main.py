# Import classes from modules
from student import Student
from product import Product

# Initialize database lists
students_db = []
products_db = []

print("=== Student Management Test ===")
# Create student instances
s1 = Student(1, "Ali", "Rezai", 18.5, 21)
s2 = Student(2, "Sara", "Ahmadi", 19.0, 22)

# Add students
Student.add_student(students_db, s1)
Student.add_student(students_db, s2)

# Display all students
print("\n--- Student List ---")
for s in students_db:
    s.display_info()

# Remove student
Student.remove_student(students_db, 1)


print("\n=== Product Management Test ===")
# Create product instances
p1 = Product(1, "Laptop", 1200, 10, "Electronics")
p2 = Product(2, "Mouse", 25, 50, "Accessories")

# Add products
Product.add_product(products_db, p1)
Product.add_product(products_db, p2)

# Display all products
print("\n--- Product List ---")
for p in products_db:
    p.display_info()

# Remove product
Product.remove_product(products_db, 2)
