class Price23Vat:
    def __init__(self, brutto: int):
        self._brutto = brutto
        self._netto = brutto / 1.23
        self._tax = brutto - self._netto

    def get_netto(self):
        return self._netto

    def get_brutto(self):
        return self._brutto

    def get_tax(self):
        return self._tax

    def set_netto(self, value):
        self._netto = value
        self._brutto = value * 1.23
        self._tax = self._brutto - self._netto

    def set_brutto(self, value):
        self._brutto = value
        self._netto = value / 1.23
        self._tax = self._brutto - self._netto

    def set_tax(self, value):
        self.set_brutto(value / 1.23)

cena = Price23Vat(10000)
print(cena._netto)
print(cena._brutto)
print(cena._tax)
print("------------------------------------")
cena.set_netto(3658)
print(cena._netto)
print(cena._brutto)
print(cena._tax)
print("------------------------------------")
cena.set_brutto(8000)
print(cena._netto)
print(cena._brutto)
print(cena._tax)
print("------------------------------------")
cena.set_tax(268)
print(cena._netto)
print(cena._brutto)
print(cena._tax)