import math


class Fraction:
    def __init__(self, a, b=None):
        # print(type(a))
        # print(type(b))
        if type(a) == int and type(b) == int:
            self.chisl = a
            self.znam = b
        else:
            ind = a.find('/')
            # print(ind)
            self.chisl = int(a[:ind])
            self.znam = int(a[ind + 1:])
        # сокращение дроби
        k = 0
        while k != 1:
            k = math.gcd(self.chisl, self.znam)  # gcd-наибольший общий делитель
            self.chisl //= k
            self.znam //= k

    def numerator(self):
        return self.chisl

    def numerator1(self, new_chisl):
        self.chisl = new_chisl
        k = 0
        while k != 1:
            k = math.gcd(self.chisl, self.znam)  # gcd-наибольший общий делитель
            self.chisl //= k
            self.znam //= k

    def denominator(self):
        return self.znam

    def denominator1(self, new_znam):
        self.znam = new_znam
        k = 0
        while k != 1:
            k = math.gcd(self.chisl, self.znam)  # gcd-наибольший общий делитель
            self.chisl //= k
            self.znam //= k

    def __add__(self, other):
        new_c = Fraction(1, 1)
        new_c.chisl = self.chisl * other.znam + other.chisl * self.znam
        new_c.znam = self.znam * other.znam
        k = 0
        while k != 1:
            k = math.gcd(new_c.chisl, new_c.znam)  # gcd-наибольший общий делитель
            new_c.chisl //= k
            new_c.znam //= k
        return new_c

    def __sub__(self, other):
        new_c = Fraction(1, 1)
        new_c.chisl = self.chisl * other.znam - other.chisl * self.znam
        new_c.znam = self.znam * other.znam
        k = 0
        while k != 1:
            k = math.gcd(new_c.chisl, new_c.znam)  # gcd-наибольший общий делитель
            new_c.chisl //= k
            new_c.znam //= k
        return new_c

    def __iadd__(self, other):
        self.chisl = self.chisl * other.znam + other.chisl * self.znam
        self.znam = self.znam * other.znam
        k = 0
        while k != 1:
            k = math.gcd(self.chisl, self.znam)  # gcd-наибольший общий делитель
            self.chisl //= k
            self.znam //= k
        return self

    def __isub__(self, other):
        self.chisl = self.chisl * other.znam - other.chisl * self.znam
        self.znam = self.znam * other.znam
        k = 0
        while k != 1:
            k = math.gcd(self.chisl, self.znam)  # gcd-наибольший общий делитель
            self.chisl //= k
            self.znam //= k
        return self

    def __str__(self):
        return f'{self.chisl}/{self.znam}'

    def __repr__(self):
        return f'Fraction({self.chisl},{self.znam})'


a = Fraction(1, 3)
b = Fraction(1, 9)
c = a + b
print(a, b, c, a is c, b is c)
a = Fraction(1, 3)
b = Fraction(1, 9)
v = a - b
print(a, b, v, a is v, b is v)
a = Fraction(1, 8)
c = b = Fraction(3, 8)
a += b
print(a, b, c, b is c)
a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)
