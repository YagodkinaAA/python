summa = 0


def recursive_digit_sum(num):
    last_num = num % 10
    global summa
    summa += last_num
    num //= 10
    if num != 0:
        recursive_digit_sum(num)
    return summa

#почему надо делить на 2(не совсем понимаю принцип работы)
def digit_sum(num):
    last_num = num % 10
    if num==0:
        return 0
    else:
        return round((last_num+recursive_digit_sum(num//10))/2)






print(recursive_digit_sum(123))
print(summa)
print(digit_sum(123))
