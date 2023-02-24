s = input()
n = s[1:]
n = int(n)
print(n)
p = []
for i in range(n):
    h = input('Введите строку:\n')
    if '#' in h:
        g = h.index('#')
        h = h[:g]
    h = h.rstrip()
    p.append(h)
for j in p:
    print(j)
