# main.py

from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    pm = ProductManager()

    product1 = Product("Coffee", 10, 50)
    product2 = Product("Tea", 20, 30)
    product3 = Product("Banana", 30, 70)
    product4 = Product("Apple", 50, 4)

    pm.add_product(product1)
    pm.add_product(product2)
    pm.add_product(product3)
    pm.add_product(product4)

    cart = Cart()
    
    if len(pm.products) >= 3:
        selected_products = random.sample(pm.products, 3)
        for prod in selected_products:
            cart.add_to_cart(prod)
    
if __name__ == "__main__":
    main()
