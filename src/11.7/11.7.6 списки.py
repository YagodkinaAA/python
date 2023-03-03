n = (input('введите строку из цифр:\n')).split()
for i in range(len(n)):
    n[i] = int(n[i])
line = [m ** 3 for m in n]
for i in line:
    print(i, end=' ')
