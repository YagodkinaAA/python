def make_list(length, value=0):
    p = [value for _ in range(length)]
    return p


print(make_list(3))
print(make_list(5, 1))
