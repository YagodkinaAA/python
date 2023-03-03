# объявление функции
def factor(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f


def compute_binom(n, k):
    binom = factor(n) / (factor(k) * (factor(n - k)))
    binom = int(binom)
    return binom


# считываем данные
n = int(input('введите число:\n'))
k = int(input('введите число:\n'))

# вызываем функцию
print('разложение в бином=', compute_binom(n, k))
