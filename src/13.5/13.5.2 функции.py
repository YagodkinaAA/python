# объявление функции
def is_prime(num):
    col = 0
    for i in range(1, num + 1):
        if num % i == 0:
            col += 1
    if col == 2:
        return True
    else:
        return False


# считываем данные
n = int(input('введите число:\n'))

# вызываем функцию
print(is_prime(n))
