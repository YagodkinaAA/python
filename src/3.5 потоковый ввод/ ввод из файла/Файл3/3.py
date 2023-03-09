# Напишите простую утилиту, которая очищает заданный файл от:повторяющихся пробелов;повторяющихся символов перевода строки;табуляций,излишних пробелов в начале и конце строк
import codecs

p = []
s = []
file1 = codecs.open('first.txt', 'r', 'utf-8')
for line in file1:
    p.append(line.rstrip('\n').split())
file1.close()
print(p)
file2 = codecs.open('second.txt', 'w', 'utf-8')
for d in p:
    for i in range(len(d)):
        if len(d) != 0:
            file2.write(d[i])
            file2.write(' ')
    if len(d) != 0:
        file2.write('\n')
file2.close()
