p = []
s = []
file1 = open('first.txt', 'r')
for line in file1:
    p.extend(line.rstrip('\n').split(' '))
file1.close()
file2 = open('second.txt', 'r')
for line in file2:
    s.extend(line.rstrip('\n').split(' '))
file2.close()
print(p)
print(s)
for a in s:
    if a not in p:
        p.append(a)
print(*p)
p.sort()
file3 = open('answer.txt', 'w')
for d in p:
    file3.write(d)
    file3.write('\n')
file3.close()
