s = input('ведите строку, состоящую из чисел:\n').split()
h = '+'
for i in range(len(s)):
    s[i] = int(s[i])
    print(h * s[i])
