# cart.py
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Proizvod {product.name} je dodat u korpu.")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart_items)
        return total

    def display_cart(self):
        for product in self.cart_items:
            print(product.display_info())
