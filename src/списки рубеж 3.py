s = input('введите строку, состоящую из чисел:\n').split()
for i in range(len(s)):
    s[i] = int(s[i])
print(*s, sep='+', end=f'={sum(s)}')
