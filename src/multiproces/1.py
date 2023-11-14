import time
import multiprocessing
from multiprocessing import Process


def test():
    for i in range(3):
        print(f"{Process.name} - {i}")
        time.sleep(1)


if __name__ == '__main__':
    pr = Process(target=test)
    Process.name = 'er'
    pr.start()
    #pr.join()
    #time.sleep(5)
    #pr.terminate() убрать процесс
    print('Процесс запущен')
    print(pr.is_alive())
    print(pr.pid)
    pr.terminate()
    time.sleep(10)
    print(pr.is_alive())

