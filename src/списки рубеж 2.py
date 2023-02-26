L = input('введите строку, состоящую из чисел:\n').split()
M = input('введите строку, состоящую из чисел:\n').split()
for i in range(len(M)):
    L[i] = int(L[i])
    M[i] = int(M[i])
p = []
for i in range(len(L)):
    s = L[i] + M[i]
    p.append(s)
print(*p)
