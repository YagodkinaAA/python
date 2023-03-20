'''Разработайте класс Rectangle.
При инициализации класс принимает два кортежа рациональных координат противоположных углов прямоугольника (со сторонами параллельными осям координат).
Класс должен реализовывать методы:
perimeter — возвращает периметр прямоугольника;
area — возвращает площадь прямоугольника'''
from math import *

class Rectangle:
    def __init__(self, a, b):
        self.x1 = a[0]
        self.y1 = a[1]
        self.x2 = b[0]
        self.y2 = b[1]
        self.x = self.x1
        self.y = self.y2
        self.lenght = sqrt((self.x2 - self.x) ** 2 + (self.y2 - self.y) ** 2)
        self.widht = sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)

    def perimeter(self):
        return round(2 * (self.lenght + self.widht),2)

    def area(self):
        return round(self.lenght * self.widht,2)


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
