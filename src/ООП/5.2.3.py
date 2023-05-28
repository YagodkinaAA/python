import math


class Point:

    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.len = 0

    def move(self, c, d):
        self.x = self.x + c
        self.y = self.y + d

    def length(self, n_point):
        self.len = math.sqrt((n_point.x - self.x) ** 2 + (n_point.y - self.y) ** 2)
        return round(self.len, 2)


class PatchedPoint(Point):
    def __init__(self, *coord):
        if len(coord) == 1:
            super().__init__(a=coord[0][0], b=coord[0][1])
        elif len(coord) == 0:
            super().__init__(a=0, b=0)
        elif len(coord) == 2:
            super().__init__(a=coord[0], b=coord[1])

    def __add__(self, *other):
        point = PatchedPoint()
        point.x = self.x + other[0][0]
        point.y = self.y + other[0][1]
        return point

    def __iadd__(self, *other):
        self.x += other[0][0]
        self.y += other[0][1]
        return self

    def __str__(self):
        return f"({self.x},{self.y})"


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
