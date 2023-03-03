# объявление функции
def get_factors(num):
    p = []
    for i in range(1, num + 1):
        if num % i == 0:
            p.append(i)
    return p


# считываем данные
n = int(input('введите натуральное число:\n'))

# вызываем функцию
print(len(get_factors(n)))
