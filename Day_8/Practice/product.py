class Product:
    def __init__(self, product_id, name, price, stock_quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.category = category

    # Display product details
    def display_info(self):
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock_quantity}")
        print(f"Category: {self.category}")
        print("-------------------------")

    # Add product to list
    @staticmethod
    def add_product(product_list, product):
        product_list.append(product)
        print(f"Product '{product.name}' added successfully!")

    # Remove product by ID
    @staticmethod
    def remove_product(product_list, product_id):
        for product in product_list:
            if product.product_id == product_id:
                product_list.remove(product)
                print(f"Product with ID {product_id} removed successfully!")
                return True
        print(f"Product with ID {product_id} not found!")
        return False
