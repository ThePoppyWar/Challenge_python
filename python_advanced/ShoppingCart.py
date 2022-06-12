from itertools import count


class Product:
    next_id = count(1)
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = next(self.next_id)


class ShoppingCart:
    def __init__(self):
        self.products = dict()
        self.quantities = dict()

    def add_product(self, product: Product):
        if product.id not in self.products.keys():
            self.products.update({product.id: product})
            self.quantities.update({product.id: 1})
        else:
            self.quantities[product.id] += 1


    def remove_product(self, product: Product):
        if product.id in self.products:
            self.products.pop(product.id)
            self.quantities.pop(product.id)

    def change_product_quantity(self, product, new_quantity):
        if product.id in self.products:
            if new_quantity < 0:
                raise ValueError("Niedozwolone działanie")
            elif new_quantity == 0:
                self.remove_product(product)
            else:
                self.quantities.update({product.id: new_quantity})

    # def get_receipt(self):
    #     receipt = str()
    #     total = 0
    #     for product_id, product in self.products.items():
    #         receipt += f'{product.name} - amount: {self.quantities.get(product_id)},'\
    #                    f' price: {product.price} zł, total: {product.price * self.quantities.get(product_id)} \n'
    #         total += product.price * self.quantities.get(product_id)
    #     receipt += f'SUMA: {total}zł'
    #     return receipt

#     Zmodyfikowany get_receipt o rabat 30% za cene za dany produkt

    def get_receipt(self):
        receipt = str()
        total = 0
        for product_id, product in self.products.items():
            if self.quantities.get(product_id) < 3:
                receipt += f'{product.name} - amount: {self.quantities.get(product_id)},' \
                           f' price: {product.price} zł, total: {product.price * self.quantities.get(product_id)} \n'
                total += product.price * self.quantities.get(product_id)
            else:
                receipt += f'{product.name} - amount: {self.quantities.get(product_id)},' \
                           f' price: {product.price}zł' \
                           f' Suma: {product.price * self.quantities.get(product_id) * 0.7}\n'
                total += product.price * self.quantities.get(product_id) * 0.7
        receipt += f'Suma: {round(total, 2)}zł'
        return receipt



bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chive = Product('Chive', 1.50)
pepper = Product('Pepper', 2.35)

print(bread.id)
print(pepper.id)
print(pepper.name)
print(pepper.price)

cart = ShoppingCart()

print(cart.products)
print(cart.quantities)
print(cart.get_receipt())

cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chive)
cart.change_product_quantity(pepper, 2)

print(cart.products)
print(cart.quantities)

# cart.remove_product(bread)

print(cart.products)
print(cart.quantities)
print(cart.get_receipt())


