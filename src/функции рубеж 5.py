# объявление функции
def get_month(language, number):
    list_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
               'декабрь']
    list_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
               'november', 'december']
    if language in 'ru':
        return list_ru[num - 1]
    else:
        return list_en[num - 1]


# считываем данные

lan = input('введите язык(ru или en):\n')
num = int(input('введите номер месяца:\n'))

# вызываем функцию
print('ваш месяц:', get_month(lan, num))
