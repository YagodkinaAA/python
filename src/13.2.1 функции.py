def draw_triangle(fill, base):
    p = base // 2
    for i in range(0, p + 1):
        print(fill * i)
    for i in range(p + 1, 0, -1):
        print(fill * i)


# считываем данные
fill = input('введите символ-заполнитель:\n')
base = int(input('введите длину основания:\n'))

# вызываем функцию
draw_triangle(fill, base)
