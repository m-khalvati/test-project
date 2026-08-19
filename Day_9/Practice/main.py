# Import entity classes
from product import Product
from student import Student

print("=== Student Management Test ===")
# Create student
s1 = Student(1, "Ali", "Rezai", 18.5, 21)
s2 = Student(2, "Sara", "Ahmadi", 19.0, 22)

# Save students
s1.save_to_file()
s2.save_to_file()

# Display all students
print("\n--- Displaying Students From File ---")
Student.display_all()

# Remove student with ID
Student.remove_from_file(1)


print("\n=== Product Management Test ===")
# Create product
p1 = Product(1, "Laptop", 1200, 10, "Electronics")
p2 = Product(2, "Mouse", 25, 50, "Accessories")

# Save products
p1.save_to_file()
p2.save_to_file()

# Display all products
print("\n--- Displaying Products From File ---")
Product.display_all()

# Remove product with ID 2
Product.remove_from_file(2)
