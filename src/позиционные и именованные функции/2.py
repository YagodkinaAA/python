def make_matrix(size, value=0):
    p = []
    k = []
    for _ in range(size[0]):
        p.append(value)
    k = [p for _ in range(size[1])]
    return k

print(*make_matrix((4, 2), value=1), sep='\n')
#print(make_matrix(3))
