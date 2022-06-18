class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dos_1 = Dog("Czarus", "Haski")
dos_2 = Dog("Oczek", "ratlerek")
dos_3 = Dog("Kiler", "doberman")

print(dos_1.name)
print(dos_2.breed)
print(dos_3.name, dos_3.breed)