p = []
col = 0
summa = 0
maxi = 0
minim = 0
file1 = open('файл1.txt', 'r')
for line in file1:
    p.extend(line.rstrip('\n').split(' '))
file1.close()
file2 = open('файл2.txt', 'w')
file2.write(f'Кол-во символов в файле: {len(p)}\n')
for f in p:
    f = int(f)
    if f > maxi:
        maxi = f
    if f < minim:
        minim = f
    summa += f
    if f > 0:
        col += 1
file2.write(f'Кол-во положительных элементов в файле: {col}\n')
file2.write(f'Минимальное число файла: {minim}\n')
file2.write(f'Максимальное число файла: {maxi}\n')
file2.write(f'Сумма всех чисел файла: {summa}\n')
file2.write(f'Среднее арифметическое всех чисел файла: {round(summa / len(p), 2)}')
file2.close()
