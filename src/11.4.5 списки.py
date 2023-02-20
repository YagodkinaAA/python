n=int(input('введите кол=во строк:\n'))
p=[]
for i in range(n):
    s=input()
    p.append(s)
d=input('введите строку:\n').lower()
for j in p:
    t=j.lower()
    if d in t:
        print('ваш поисковый запрос выполнен:\n'j)

