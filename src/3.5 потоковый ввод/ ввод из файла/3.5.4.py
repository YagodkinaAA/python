#Создайте программу, которая реализует маленький компонент поисковой системы.Формат ввода.Вводятся заголовки страниц.В последней строке записан поисковый запрос.
from sys import stdin
p = []
k = []
zapr=[]
for line in stdin:
    p.append(line.rstrip('\n').split())
print(p)
col = len(p)
zapr=p[col-1]
#z=str(p[col-1.2]).lower()
#zapr.append(z)
print(zapr)
k=p[:col-1]
print(k)
print(p)
for i in range(len(k)):
    flag=0
    for j in range(len(k[i])) :
        k[i][j]=k[i][j].lower()
        if k[i][j] in zapr:
            flag=1
            print(i,k[i])
            print(p[i])
            break
