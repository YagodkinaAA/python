# объявление функции
def convert_to_python_case(text):
    s = ''
    index1 = 0
    index2 = 0
    for i in range(1, len(text)):
        if 65 <= ord(text[i]) <= 90:
            index2 = i
            s += text[index1:index2] + '_'
            index1 = index2
    s += text[index2:]
    s = s.lower()
    return s


# считываем данные
txt = input('введите строку в "верблюжьем" регистре:\n')

# вызываем функцию
print(convert_to_python_case(txt))
