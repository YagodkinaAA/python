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
n += 1
while not is_prime(n):
    n += 1
print(n)
