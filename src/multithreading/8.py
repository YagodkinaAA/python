import time
from threading import Thread, BoundedSemaphore, current_thread
import random


max_connections = 5 #максимальное кол-во потоков, которые могут работать одновременно
pool = BoundedSemaphore(value=max_connections) #создали блокировщик в виде семафора


def test():
    with pool: #используем блокировщик
        slp = random.randint(1, 5) #сгенерировали рандомную задержку
        print(f'{current_thread().name} - sleep({slp})')
        time.sleep(slp)

for i in range(10):
    Thread(target=test, name=f'thr-{i}').start()