# объявление функции
def is_one_away(word1, word2):
    col = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                col += 1
        if col == len(word1) - 1:
            return True
        else:
            return False
    else:
        return False


# считываем данные
txt1 = input('введите слово:\n')
txt2 = input('введите слово:\n')

# вызываем функцию
print(is_one_away(txt1, txt2))
