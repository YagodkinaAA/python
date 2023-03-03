# объявление функции
def is_valid_password(password):
    if len(password) != 3:
        return False
    else:
        col = 0
        flag = 0
        sol = 0
        a = password[0]
        b = int(password[1])
        c = int(password[2])
        for i in range(len(a) // 2):
            if a[i] == a[len(a) - 1 - i]:
                flag += 1
        if flag == len(a) // 2:
            col += 1
        for j in range(1, b + 1):
            if b % j == 0:
                sol += 1
        if sol == 2:
            col += 1
        if c % 2 == 0:
            col += 1
        if col == 3:
            return True
        else:
            return False


# считываем данные
psw = [m for m in input('введите пароль:\n').split(':')]

# вызываем функцию
print(is_valid_password(psw))
