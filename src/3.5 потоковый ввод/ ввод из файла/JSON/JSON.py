import json
from sys import stdin

slov = []
print('введите строки вида ключ == значение')
for line in stdin:
    slov.append(line.rstrip('\n').split(' '))
#print(slov)
with open("data.json", encoding="UTF-8") as file1:
    value = json.load(file1)
#print(value)
for f in slov:
    value[f[0]] = f[2]
#print(value)
with open("data1.json", 'w', encoding="UTF-8") as file2:
    json.dump(value, file2, ensure_ascii=False, indent=2)
