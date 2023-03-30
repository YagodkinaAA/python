def make_equation(*num):
    if len(num) == 1:
        return num[0]
    else:
        (*first, last) = num
        return f'({make_equation(*first)}) * x + {last}'


print(make_equation(3, 2, 1, 5))
