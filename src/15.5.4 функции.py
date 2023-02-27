# объявление функции
def is_password_good(password):
    col = 0
    flag = 0
    if len(password) >= 8:
        col += 1
    if password.islower() == False:
        col += 1
    if password.isupper() == False:
        col += 1
    for i in range(len(password)):
        if password[i] in '1234567890':
            flag += 1
    if flag > 0 and flag != len(password):
        col += 1
    if col == 4:
        return True
    else:
        return False


# считываем данные
txt = input('введите пароль:\n')

# вызываем функцию
print(is_password_good(txt))
