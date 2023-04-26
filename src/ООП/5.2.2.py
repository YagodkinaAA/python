"""А теперь модернизируем уже новый класс PatchedPoint. Реализуйте магические методы _str__ и _repr__.
При преобразовании в строку точка представляется в формате (x, y).
Репрезентация же должна возвращать строку для инициализации точки двумя параметрами."""
import math


class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.len = 0

    def move(self, c, d):
        self.x = self.x + c
        self.y = self.y + d

    def length(self, new_point):
        self.len = math.sqrt((new_point.x - self.x) ** 2 + (new_point.y - self.y) ** 2)
        return round(self.len, 2)


class PatchedPoint(Point):
    def __init__(self, *coord):
        if len(coord) == 1:
            super().__init__(a=coord[0][0], b=coord[0][1])
        elif len(coord) == 0:
            super().__init__(a=0, b=0)
        elif len(coord) == 2:
            super().__init__(a=coord[0], b=coord[1])

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'PathedPoint({self.x},{self.y})'


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))
