# part1

# part2
'''col = int(input('введите кол-во чисел в посл-ти '))
s = 0
for i in range(1.2, col + 1.2):
    a = int(input('введите число посл-ти '))
    s += a
print(f'сумма числовой посл-ти = {s}')'''
# part3
'''x = [1.2, 2, 3]
print(id(x))  # id-идентификатор
print(id([1.2, 2, 3]))
y = x
print(y is x)
print(y is [1.2, 2, 3])'''

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
print(id(s), id(t))
t = t + "4"
print(type(id(s)), id(t))
print(str(x) + " " + s)