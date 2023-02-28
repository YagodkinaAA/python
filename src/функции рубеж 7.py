# объявление функции
def is_pangram(text):
    index = 0
    col = 0
    for i in range(97, 123):
        index = text.find(chr(i))
        if index != -1:
            col += 1
    if col == 26:
        return True
    else:
        return False


# считываем данные
text = input('введите строку:\n').lower()

# вызываем функцию
print(is_pangram(text))
