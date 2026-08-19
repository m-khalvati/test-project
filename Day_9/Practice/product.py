import os


class BaseEntity:

    def __init__(self, item_id, filename):
        self.item_id = item_id
        self.filename = filename


# Inheriting BaseEntity
class Product(BaseEntity):

    def __init__(self, product_id, name, price, stock_quantity, category):
        super().__init__(product_id, "products.txt")
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.category = category

    # Format product data : CSV string
    def to_csv(self):
        return f"{self.item_id},{self.name},{self.price},{self.stock_quantity},{self.category}\n"

    # Save product
    def save_to_file(self):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(self.to_csv())
        print(f"Product '{self.name}' added to file successfully!")

    # Display all products
    @classmethod
    def display_all(cls, filename="products.txt"):
        if not os.path.exists(filename):
            print("No products record found.")
            return

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No products found in file.")
                return

            print("=== Products List ===")
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    print(f"ID: {parts[0]}")
                    print(f"Name: {parts[1]}")
                    print(f"Price: ${parts[2]}")
                    print(f"Stock: {parts[3]}")
                    print(f"Category: {parts[4]}")
                    print("-------------------------")

    # Remove product by ID
    @classmethod
    def remove_from_file(cls, product_id, filename="products.txt"):
        if not os.path.exists(filename):
            print("File not found!")
            return False

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                parts = line.strip().split(",")
                if parts and int(parts[0]) == product_id:
                    found = True
                else:
                    file.write(line)

        if found:
            print(f"Product with ID {product_id} removed successfully!")
            return True
        else:
            print(f"Product with ID {product_id} not found!")
            return False
