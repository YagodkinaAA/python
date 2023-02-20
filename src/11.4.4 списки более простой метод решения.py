p = []
n = int(input('Введите кол-во строк\n'))
for i in range(n):
    a = input('Введите строку:\n')
    if a not in p:
        p.append(a)
print('Неповторяющиеся строки:')
for f in p:
    print(f)
