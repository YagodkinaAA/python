# Напишите программу, которая находит сумму всех чисел введённых пользователем.(пользователь вводит несколько строк из чисел)
from sys import stdin

p = []
s = []
for line in stdin:
    p.append(line.split())
print(p)
for f in p:
    for i in range(len(f)):
        f[i] = int(f[i])
        s.append(f[i])
print(sum(s))
