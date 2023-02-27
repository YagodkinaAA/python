# объявление функции
def get_days(month):
    col = 0
    if month == 2:
        col = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        col = 30
    else:
        col = 31
    return col


# считываем данные
num = int(input('введите номер месяца:\n'))

# вызываем функцию
print('Кол-во дней в месяце:', get_days(num))
