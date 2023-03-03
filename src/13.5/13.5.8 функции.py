def is_correct_bracket(text):
    col = 0
    for i in range(len(text)):
        if text[i] in '(':
            col += 1
        if text[i] in ')':
            col -= 1
        if col < 0:
            return False
    if col == 0:
        return True
    else:
        return False


# считываем данные
txt = input('введите выражение состоящее из скобочек:\n')

# вызываем функцию
print(is_correct_bracket(txt))
