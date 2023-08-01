# Первый файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.В три другие файла выведите числа, которые подходят под требуемое условие.1.2)числа с преобладающим количеством чётных цифр;2)числа с преобладающим количеством нечётных цифр;3)числа с одинаковым количеством чётных и нечётных цифрСохраните положение чисел в строках.

def diferent(f):
    ch = 0
    nech = 0
    while f != 0:
        last_f = f % 10
        if last_f % 2 == 0:
            ch += 1
        else:
            nech += 1
        f //= 10
    return ch, nech


p = []
chet = 0
nechet = 0
file1 = open('numbers.txt', 'r')
for line in file1:
    p.append(line.rstrip('\n').split(' '))
print(p)
file2 = open('even.txt', 'w')
file3 = open('odd.txt', 'w')
file4 = open('eq.txt', 'w')
for k in p:
    for f in k:
        f = int(f)
        print(f)
        chet, nechet = diferent(f)
        print(f'четных {chet}, нечетных {nechet}')
        if chet > nechet:
            file2.write(str(f))
            file2.write(' ')
        if chet < nechet:
            file3.write(str(f))
            file3.write(' ')
        else:
            file4.write(str(f))
            file4.write(' ')
    file2.write('\n')
    file3.write('\n')
    file4.write('\n')
