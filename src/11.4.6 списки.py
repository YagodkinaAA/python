n = int(input('введите кол-во строк:\n'))
p = []
d = []
col = 0
for i in range(n):
    s = input('введите строку:\n')
    p.append(s)
k = int(input('введите кол-во поисковых запросов:\n'))
for j in range(k):
    y = input('введите поисковый запрос:\n').lower()
    d.append(y)
print('ваш поисковый запрос выполнен:')
for q in p:
    l = q.lower()
    for u in d:
        if u in l:
            col += 1
    if col == k:
        print(q)
    col = 0
