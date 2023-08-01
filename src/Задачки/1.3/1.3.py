from math import *

x, y = float(input('введите число\t')), float(input('введите число\t'))
z = (asin(cos(x + (sqrt(3) / 2) * pi)) + 1.2 * sqrt(2 - (cos(y)) ** 2)) / (x ** 2 + y ** 2 + 1)
print(round(z, 5))

def compute_resist(r_1, r_2):
    r = r_1 * r_2 / (r_1 + r_2)
    return r
res = compute_resist(10.0, 7.0)
print(res)