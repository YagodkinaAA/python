# Напишите программу, которая выполняет данную функцию за интерпретатор(удаляет комментарии).Формат ввода:Вводятся строки программы.
from sys import stdin

p = []
s = []
d = []
for line in stdin:
    p.append(line.rstrip('\n').split())
for f in p:
    for i in range(len(f)):
        if f[i] not in '#':
            s.append(f[i])
        else:
            break
    a = ' '.join(s)
    d.append(a)
    s.clear()
print('Все комментарии удалены:\n')
for q in d:
    if q not in '':
        print(q)
