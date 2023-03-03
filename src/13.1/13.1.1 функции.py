# объявление функции
def draw_box():
    s1 = '*'
    s2 = ' '
    for i in range(14):
        if i == 0 or i == 13:
            print(s1 * 10)
        else:
            print(s1 + s2 * 8 + s1)


# основная программа
draw_box()  # вызов функции
