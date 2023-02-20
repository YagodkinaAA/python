n=int(input('введите кол-во чисел:\n'))
p=[]
for i in range(n):
    g=int(input('введите число:\n'))
    p.append(g)
for j in p:
    if j<0:
        print(j)
for j in p:
    if j==0:
        print(j)
for j in p:
    if j>0:
        print(j)

