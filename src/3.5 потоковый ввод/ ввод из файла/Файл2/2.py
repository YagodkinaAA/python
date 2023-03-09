import codecs
p = []
s = []
file1 = codecs.open('first.txt', 'r','utf-8')
for line in file1:
    p.extend(line.rstrip('\n').split(' '))
file1.close()
file2 = codecs.open('second.txt', 'r','utf-8')
for line in file2:
    s.extend(line.rstrip('\n').split(' '))
file2.close()
print(p)
print(s)
for a in s:
    if a not in p:
        p.append(a)
p.sort()
print(*p)
file3 = codecs.open('answer.txt', 'w','utf-8')
for d in p:
    file3.write(d)
    file3.write('\n')
file3.close()
