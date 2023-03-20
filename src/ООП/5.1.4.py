'''Рассмотрим объект «Программист», который задаётся именем, должностью и количеством отработанных часов. Каждая должность имеет собственный оклад (заработную плату за час работы). В нашей импровизированной компании существуют 3 должности:
Junior — с окладом 10 тугриков в час;
Middle — с окладом 15 тугриков в час;
Senior — с окладом 20 тугриков в час по умолчанию и +1 тугрик за каждое новое повышение.
Напишите класс Programmer, который инициализируется именем и должностью (отработка у нового работника равна нулю). Класс реализует следующие методы:
work(time) — отмечает новую отработку в количестве часов time;
rise() — повышает программиста;
info() — возвращает строку для бухгалтерии в формате: <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.'''
class Programmer:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.time = 0
        self.money = 0
        self.flag = 0
        self.time1 = 0

    def work(self, time):
        a = 'Junior'
        b = 'Middle'
        c = 'Senior'
        self.time = time
        self.time1 += time
        if self.job in a:
            self.money += self.time * 10
        elif self.job in b:
            self.money += self.time * 15
        elif self.job in c:
            self.money += self.time * (20 + self.flag)

    def rise(self):
        a = 'Junior'
        b = 'Middle'
        c = 'Senior'
        if self.job in a:
            self.job = b
        elif self.job in b:
            self.job = c
        elif self.job in c:
            self.flag += 1

    def info(self):
        return f'{self.name} {self.time1}ч. {self.money}тгр.'

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
