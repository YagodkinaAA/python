# Пользователь вводит количество строк которые он хочет увидеть из файла.
import codecs

n = int(input('Введите кол-во строк, которые вы хотите вывести на экран:\n'))
col = 0
file1 = codecs.open('some_file.txt', 'r', 'utf-8')
lines = len(file1.readlines())
file1.close()
file1 = codecs.open('some_file.txt', 'r', 'utf-8')
for line in file1:
    col += 1
    if lines - n < col <= lines:
        print(line, end='')
file1.close()
