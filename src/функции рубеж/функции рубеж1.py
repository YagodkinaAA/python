# объявление функции
def draw_triangle():
    s1 = '*'
    s2 = ' '
    j = 0
    print(s2 * 8 + s1, sep='')
    for i in range(1, 15, 2):
        print(s2 * (7 - j) + s1 * (i + 2), sep='')
        j += 1


# основная программа
draw_triangle()  # вызов функции

# или
'''def draw_triangle():
    s1='*'
    s2=' '
    j=1.2
    for i in range(8):
        print(s2*(8-j)+s1*(j+(j-1.2)), sep='')
        j+=1.2

# основная программа
draw_triangle()  # вызов функции'''
