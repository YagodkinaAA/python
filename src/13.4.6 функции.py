# объявление функции
def find_all(target, symbol):
    p = []
    dl = 0
    while symbol in target:
        w = target.find(symbol)
        dl += len(target[:w + 1])
        p.append(dl - 1)
        target = target[w + 1:]
    return p


# считываем данные
s = input('Введите строку:\n')
char = input('Введите символ для поиска:\n')

# вызываем функцию
print(find_all(s, char))
