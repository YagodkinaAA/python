# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep='')


# считываем данные
name, surname, patronymic = input('введите имя:\n').upper(), input('введите фамилию:\n').upper(), input(
    'введите отчество:\n').upper()

# вызываем функцию
print_fio(name, surname, patronymic)
