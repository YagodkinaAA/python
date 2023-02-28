# объявление функции
def is_magic(date):
    a = date[0] * date[1]
    b1 = date[2] % 10
    b2 = date[2] // 10 % 10
    b = b2 * 10 + b1
    if a == b:
        return True
    else:
        return False


# считываем данные
date = [int(m) for m in input('введите дату рождения(день.месяц.год):\n').split('.')]

# вызываем функцию
print(is_magic(date))
