from math import sqrt


class Shape:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def discribe(self):
        return f'The Shape has: x = {self.x}, y = {self.y} and color = {self.color}'

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"

shape_1= Shape(3, 6, "black")
shape_2 = Shape(1, 2, "green")

print(shape_1)
print(shape_2)

print(shape_1.distance(shape_2))
print(shape_2.distance(shape_1))
print("++++++++++++++++++++++++++++++++++++")

print(shape_1.discribe())

