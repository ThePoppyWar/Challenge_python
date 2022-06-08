import math


class Square:
    def __init__(self, side):
        self._side = side
        self._perimeter = 4 * side
        self._area = side * side
        self._diagonal = math.sqrt(2) * side

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_side: int or float):
        self._side = new_side
        self._perimeter = 4 * self._side
        self._area = self._side * self._side
        self._diagonal = math.sqrt(2) * self._side

    def set_perimeter(self, new_length):
        self.set_side(new_length / 4)

    def set_area(self, new_area):
        self.set_side(new_area ** 0.5)

    def set_diagonal(self, new_length):
        self.set_side(new_length/ math.sqrt(2))


