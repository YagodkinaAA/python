n = int(input("Введите количество чисел "))
p = []
n = int(input('ведите количество чисел:\n'))
for i in range(n):
    a = int(input("Введите число ")) ** 3
    p.append(a)
minim = min(p)
maxim = max(p)
for j in p :
    if j==maxim or j == minim:
        continue
    print(j)

