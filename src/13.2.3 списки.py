# объявление функции
def print_digit_sum(num):
    summa = 0
    while num > 0:
        last = num % 10
        summa += last
        num //= 10
    print('сумма цифр =', summa)


# считываем данные
n = int(input('введите число:\n'))

# вызываем функцию
print_digit_sum(n)
