# Напишите программу, которая определяет, на сколько изменился средний рост учеников в классе.(Формат ввода:<Имя> <Рост месяц назад> <Рост сейчас>)
from sys import stdin

p = []
col = 0
razn = 0
for line in stdin:
    p.append(line.rstrip('\n').split())
    col += 1
for f in p:
    for i in range(1):
        v = int(f[i + 2]) - int(f[i + 1])
        razn += v
print(f'В среднем рост ученика изменился на {round(razn / col)}')
