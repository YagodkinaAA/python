# объявление функции
def is_palindrome(text):
    d = ''
    d1 = ''
    for i in range(len(text)):
        if text[i] in 'qwertyuioplkjhgfdsazxcvbnm' or text[i] in 'йцукенгшщзхъэждлорпавыфячсмитьбю':
            d += text[i]
    for j in range(len(d) - 1, -1, -1):
        d1 += d[j]
    if d1 in d:
        return True
    else:
        return False


# считываем данные
txt = input('введите строку:\n').lower()
# вызываем функцию
print(is_palindrome(txt))
