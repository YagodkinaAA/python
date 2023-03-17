def make_matrix(*size, value=0):
    p = []
    if type(size[0]) == int:
        rows = size[0]
        cols = size[0]
    else:
        rows = size[0][1]
        cols = size[0][0]

    for _ in range(rows):
        p.append([value for _ in range(cols)])
    return p


print(*make_matrix((4, 2), value=1), sep='\n')
print(*make_matrix(3), sep='\n')