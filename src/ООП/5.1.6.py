'''Расширим функционал класса написанного вами в предыдущей задаче.
Реализуйте методы:
get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
get_size() — возвращает размеры в виде кортежа;
move(dx, dy) — изменяет положение на заданные значения;
resize(width, height) — изменяет размер (положение верхнего левого угла остаётся неизменным).'''
from math import *


class Rectangle:
    def __init__(self, a, b):
        self.x1 = a[0]
        self.y1 = a[1]
        self.x2 = b[0]
        self.y2 = b[1]
        self.x = min(self.x1, self.x2)
        self.y = max(self.y1, self.y2)

        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
            self.y1, self.y2 = self.y2, self.y1

        if self.y == self.y2:
            self.lenght = round(sqrt((self.x2 - self.x) ** 2 + (self.y2 - self.y) ** 2), 2)
            self.widht = round(sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2), 2)
        else:
            self.xnew = self.x2
            self.ynew = self.y1
            self.lenght = round(sqrt((self.x1 - self.xnew) ** 2 + (self.y1 - self.ynew) ** 2), 2)
            self.widht = round(sqrt((self.xnew - self.x2) ** 2 + (self.ynew - self.y2) ** 2), 2)

    def get_pos(self):
        pos = (round(self.x, 2), round(self.y, 2))
        return pos

    def get_size(self):
        size = (self.lenght, self.widht)
        return size

    def move(self, dx, dy):
        self.x1 = self.x1 + dx
        self.y1 = self.y1 + dy
        self.x2 = self.x2 + dx
        self.y2 = self.y2 + dy
        self.x = self.x + dx
        self.y = self.y + dy

    def resize(self, m, n):
        self.lenght = m
        self.widht = n


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
