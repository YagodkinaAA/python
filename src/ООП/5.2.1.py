"""Создайте класс PatchedPoint — наследника уже написанного вами Point.
Требуется реализовать следующие виды инициализации нового класса:
параметров не передано — координаты точки равны 0;
передан один параметр — кортеж с координатами точки;
передано два параметра — координаты точки"""
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


point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
first_point = PatchedPoint((2, -7))
print(first_point.x, first_point.y)
second_point = PatchedPoint(7, 9)
print(second_point.x, second_point.y)
print(first_point.length(second_point))
print(second_point.length(first_point))
