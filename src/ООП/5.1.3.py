# Напишите класс RedButton, который описывает красную кнопку.Класс должен реализовывать методы:click() — эмулирует
# нажатие кнопки, выводит сообщение "Тревога!";count() — возвращает количество раз, которое была нажата кнопка.
class RedButton:
    def __init__(self):
        self.col = 0

    def click(self):
        self.col += 1
        return 'Тревога!'

    def count(self):
        return self.col


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        print(second_button.click())
    else:
        print(first_button.click())
print(first_button.count(), second_button.count())
