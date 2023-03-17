# не знаю как скобочки доставить и убрать 0 в конце
def make_equation(*num):
    if len(num) == 0:
        return 0
    else:
        return f'({str(num[0])})*x)+{str(make_equation(*num[1:]))}'


print(make_equation(3, 1, 5))
