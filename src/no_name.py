import math


def sign(num):
    if num < 0:
        return -1
    else:
        return 1


a = -5
b = 3
print(a / b)
print(a // b)
print(min(math.fabs(a), b))
print(sign(a))
