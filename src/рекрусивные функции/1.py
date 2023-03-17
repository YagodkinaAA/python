#функция при помощи цикла
def summator(*num):
    summa = 0
    for i in range(len(num)):
        summa += num[i]
    return summa

#функция при помощи рекрусии
def recursive_sum(*num):
    if len(num) == 0:
        return 0
    return num[0] + recursive_sum(*num[1:])


print(summator(7, 18, 3, 2, 10))
print(recursive_sum(7, 18, 3, 2, 10))
