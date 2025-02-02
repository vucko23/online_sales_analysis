# product_manager.py

from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Proizvod {product_name} je uklonjen.")
                return
        print(f"Proizvod {product_name} nije pronadjen.")
