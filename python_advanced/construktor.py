class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # def __str__(self):
    #     return f"Breed of dog {self.breed} has a name {self.name}"
    def __repr__(self):
        return f"Breed of dog {self.breed} has a name {self.name}"


dos_1 = Dog("Czarus", "Haski")
dos_2 = Dog("Oczek", "ratlerek")
dos_3 = Dog("Kiler", "doberman")

print(dos_1)
print("_____________________________")
print(dos_1.name)
print(dos_2.breed)
print(dos_3.name, dos_3.breed)