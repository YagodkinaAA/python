# объявление функции
def merge(list1, list2):
    list2.extend(list1)
    list2.sort()
    return list2


# считываем данные
numbers1 = [int(c) for c in input('Введите 1-й отсортированный список:\n').split()]
numbers2 = [int(c) for c in input('Введите 2-й отсортированный список:\n').split()]

# вызываем функцию
print(merge(numbers1, numbers2))
