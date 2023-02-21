s = input('введите строку:\n').split()
col = 0
for i in range(len(s)):
    s[i] = int(s[i])
for j in s:
    print('j=', j)
    for u in s:
        print('u=', u)
        if j == u:
            col += 1
            print('col=', col)
t = (col - len(s)) / 2
print('кол-во пар:', int(t))
