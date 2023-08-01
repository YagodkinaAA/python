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

    def __neg__(self):
        pass

    def __str__(self):
        return f'{self.chisl}/{self.znam}'

    def __repr__(self):
        return f"Fraction('{self.chisl}/{self.znam}')"


a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))

a = Fraction('-1.2/2')
b = -a
print(-a, b, a is b)
'''b.numerator1(-b.numerator())
a.denominator1(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())'''
