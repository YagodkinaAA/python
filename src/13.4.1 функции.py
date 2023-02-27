# объявление функции
def convert_to_miles(km):
    return km*0.6214

# считываем данные
num = int(input('введите число для перевода:\n'))

# вызываем функцию
print(convert_to_miles(num))