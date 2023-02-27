def quick_merge(list1, list2):
    p1 = 0
    p2 = 0
    q = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            q.append(list1[p1])
            p1 += 1
        else:
            q.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        q += list1[p1:]
    if p2 < len(list2):
        q += list2[p2:]
    return q



n = int(input('введите кол-во списков:\n'))
a = [int(m) for m in input('введите список из чисел:\n').split()]
b = [int(m) for m in input('введите список из чисел:\n').split()]
c = quick_merge(a, b)
for _ in range(n - 2):
    d = [int(m) for m in input('введите список из чисел:\n').split()]
    c = quick_merge(c, d)
print(*c)
