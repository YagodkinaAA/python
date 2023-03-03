s = input('Введите строку, состоящую из чисел:\n').split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print('Отсортированный список:')
print(*s)
s.sort(reverse=True)
print('Отсортированный список:')
print(*s)
