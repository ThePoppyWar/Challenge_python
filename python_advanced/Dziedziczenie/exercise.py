class Cart:
    def __init__(self):
        self.products = []

    def add(self, price: float, name: str):
        self.products.append((price, name))

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):
    def summary(self):
        return [(name, price * 0.8) for name, price in self.products]


# class Discount20PercentCart(Cart):
#     def summary(self):
#         new_recipt = []
#         for name, price in self.products:
#             new_recipt.append((name, price * 0.8))
#         return new_recipt

class Above3ProductsCheapestFreeCart(Cart):
    def summary(self):
        if len(self.products) > 3:
            def get_price(product):
                return product[1]

            sorted_products = sorted(self.products, key=get_price)
            sorted_products[0] = (sorted_products[0][0], 0.0)
            return sorted_products
        else:
            return self.products

