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


