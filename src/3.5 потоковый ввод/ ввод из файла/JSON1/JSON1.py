import json

zap=dict()
with open("users.json", encoding="UTF-8") as file1:
    value = json.load(file1)
print(value)
with open("updates.json", encoding="UTF-8") as file2:
    new = json.load(file2)
print(new)
for i in range(len(value)):
    zap[value[i]['name']]=value[i]
print(zap)
for j in range(len(zap)):
    if new[j]['name'] in zap:
        zap[value[j]['name']]=new[j]
print(zap)
with open("users1.json", 'w',encoding="UTF-8") as file3:
    json.dump(zap, file3, ensure_ascii=False, indent=2)