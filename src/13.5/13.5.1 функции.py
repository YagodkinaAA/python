# объявление функции
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


# считываем данные
a, b, c = int(input('Введите сторону треугольника:\n')), int(input('Введите сторону треугольника:\n')), int(
    input('Введите сторону треугольника:\n'))

# вызываем функцию
print(is_valid_triangle(a, b, c))
