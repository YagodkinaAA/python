s = input('введите строку, состоящую из чисел:\n').split()
for i in range(len(s)):
    s[i] = int(s[i])
a = min(s)
b = max(s)
ismall = s.index(a)
ibig = s.index(b)
s[ismall] = b
s[ibig] = a
for j in s:
    print(j, end=' ')
