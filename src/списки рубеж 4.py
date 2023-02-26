p = [m for m in input('введите номер телефона:\n').split('-')]
flag = 0
col = 0
for i in range(len(p)):
    if p[i].isdigit() == True:
        col += 1
if col == 4 and '7' in p[0] and len(p[0]) == 1 and len(p[1]) == 3 and len(p[2]) == 3 and len(p[3]) == 4:
    flag = 1
elif col == 3 and len(p[0]) == 3 and len(p[1]) == 3 and len(p[2]) == 4:
    flag = 1
if flag == 1:
    print('номер корректный')
else:
    print('номер некорректный')

