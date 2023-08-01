name = str(input('Ваше имя: '))
print(f'Привет, {name}!')
age = int(input('Ваш возраст: '))
height = float(input('Ваш рост в метрах: '))
weight = float(input('Ваш вес в килограммах: '))
if age < 10 or height < 0 or height > 3 or weight < 0 or weight > 500:
    print('Ошибочные входные данные')
else:
    bmi = round(weight / height ** 2, 2)
    print(f'Ваш индекс массы тела:{bmi}')
    if age < 45:
        if bmi < 18.5:
            description = 'недостаточной массой тела'
        elif 18.5 <= bmi <= 24.99:
            description = 'нормальной массой тела'
        elif 25 <= bmi <= 29.99:
            description = 'избыточной массой тела'
        else:
            description = 'ожирением'
        print(f'Вы относитесть к группе с {description}')
    else:
        if bmi < 22:
            description = 'недостаточной массой тела'
        elif 22 <= bmi <= 26.99:
            description = 'нормальной массой тела'
        elif 27 <= bmi <= 31.99:
            description = 'избыточной массой тела'
        else:
            description = 'ожирением'
        print(f'Вы относитесть к группе с {description}')



