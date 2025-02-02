# main.py

from product import Product
from product_manager import ProductManager

def main():
    pm = ProductManager()

    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Smartphone", 500, 10)
    product3 = Product("Tablet", 300, 7)
    product4 = Product("Tv", 800, 3)

    pm.add_product(product1)
    pm.add_product(product2)
    pm.add_product(product3)
    pm.add_product(product4)

    print("Svi proizvodi:")
    pm.display_all_products()
    print("Ukupna vrijednost:", pm.total_inventory_value())

if __name__ == "__main__":
    main()
