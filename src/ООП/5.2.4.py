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

    def __str__(self):
        return f'{self.chisl}/{self.znam}'

    def __repr__(self):
        return f'Fraction({self.chisl},{self.znam})'


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction1 = Fraction('7/14')
print(fraction1, repr(fraction1))
fraction3 = Fraction(3, 210)
print(fraction3, repr(fraction3))
fraction3.numerator1(10)
print(fraction3.numerator(), fraction3.denominator())
fraction3.denominator1(2)
print(fraction3.numerator(), fraction3.denominator())
