from math import *


def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (sqrt(D) - b) / (2 * a)
        x2 = (-sqrt(D) - b) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2
    if D == 0:
        x1 = (-b) / (2 * a)
        x2 = x1
        return x1, x2
    else:
        print('уравнение имеет не имеет корней!')


a, b, c = int(input('введите коэффициент квадратного уравнения:\n')), int(
    input('введите коэффициент квадратного уравнения:\n')), int(input('введите коэффициент квадратного уравнения:\n'))
x1, x2 = solve(a, b, c)
print('Решение квадратного уравнения:', x1, x2)
