s = input('введите IP-адрес:\n').split('.')
col = 0
for i in range(len(s)):
    s[i] = int(s[i])
    if 0 <= s[i] <= 255:
        col += 1
if col == 4:
    print('IP-адрес корректный')
else:
    print('IP-адрес некорректный')
