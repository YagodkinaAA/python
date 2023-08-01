from random import *

cn = int(input('введите границу поиска:\n'))
num = randrange(n)
print(num)
value = -1
left = 1
right = n
col = 0
while value != num:
    col += 1
    value = int(input('как вы думаете какое число я загадала?:\n'))
    middle = (left + right) // 2
    if middle == num:
        print('вы угадали!\n')
        print('вам понадобилось', col, 'попыток')
    else:
        if middle < num:
            print('Ваше число ')
            left = middle + 1
    if middle > num:
        right = middle - 1
print(value)
