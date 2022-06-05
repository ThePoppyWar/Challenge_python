class Price:
    def __init__(self, price: int or float):
        self.value = float(round(price, 2))

    def __str__(self):
        return f'{self.value}zł'

    @classmethod
    def from_usd(cls, usd):
        return cls(usd * 3.8)

    @classmethod
    def from_eur(cls, eur):
        return cls(eur * 4.5)




some_price = Price.from_usd(25)
some_other_price = Price.from_eur(80)

print(some_price)
print(some_other_price)
