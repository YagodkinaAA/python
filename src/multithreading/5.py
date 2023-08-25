import time
import threading

def test():
    while True:
        print('Test')
        time.sleep(1)

thr = threading.Timer(10, test) #поставили функцию в очередь на выполнение
# interval-значение секунд, которые необходимо ждать до запуска следующего потока,
# function-функция, которую надо выполнять
thr.setDaemon(True)
thr.start()
for _ in range(6):
    print('111')
    time.sleep(2)
thr.cancel() #позволяет отменить поток до того, как он будет запущен
print('finish!')

