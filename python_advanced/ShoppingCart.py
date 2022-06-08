class Product:
    id = 1
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.id
        Product.id += 1


class ShoppingCart:
    def __init__(self):
        self.products = dict()
        self.quantities = dict()

    def add_product(self, product):
        pass

    def remove_product(self, product):
        pass

    def change_product_quantity(self, product, new_quantity):
        pass

    def get_receipt(self):
        pass




