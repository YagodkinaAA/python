# объявление функции
def get_shipping_cost(quantity):
    summa = 0
    if quantity == 1:
        summa = 1000
    else:
        summa = 1000
        for _ in range(quantity - 1):
            summa += 120
    return summa


# считываем данные
n = int(input('введите кол-во товаров:\n'))

# вызываем функцию
print('сумма доставки=', get_shipping_cost(n))
