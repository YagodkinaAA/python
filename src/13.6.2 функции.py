from math import *


def get_circle(R):
    C = 2 * pi * R
    S = pi * R ** 2
    return C, S


r = float(input('введите радиус окрожности:\n'))
length, square = get_circle(r)
print('Длина окружности=', length, 'Площадь круга=', square)
