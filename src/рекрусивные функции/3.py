def make_equation(*num):
    if len(num) == 1:
        return num[0]
    else:
        return f'({make_equation(*num[:-1])}) * x + {num[-1]}'
'''def make_equation(*num):
    if len(num) == 1:
        return num[0]
    else:
        (*first, last) = num
        return f'({make_equation(*first)}) * x + {last}'
'''

print(make_equation(3, 1, 5, 3))
