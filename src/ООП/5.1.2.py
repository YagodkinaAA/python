#Реализуйте методы:move, который перемещает точку на заданное расстояние по осям xx и yy;length, который определяет до переданной точки расстояние, округлённое до сотых.
from math import *


class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.dlina = 0

    def move(self, c, d):
        self.x = self.x + c
        self.y = self.y + d

    def lenght(self, new_point):
        self.dlina = sqrt((new_point.x - self.x) ** 2 + (new_point.y - self.y) ** 2)
        return self.dlina


point = Point(int(input('введите координату по Ох: ')), int(input('введите координату по Оу: ')))
print(point.x, point.y)
point.move(int(input('введите координату смещения по Ох: ')), int(input('введите координату смещения по Оу: ')))
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(round(first_point.lenght(second_point), 2))
print(round(second_point.lenght(first_point), 2))
