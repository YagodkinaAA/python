p = []
col=0
n = int(input())
a=input()
p.append(a)
for i in range(n-1):
    a = input()
    for u in p:
        if a in u:
            col+=1
    if col==0:
        p.append(a)
    col=0
for f in p:
    print(f)