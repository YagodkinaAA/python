import time
import threading

value = 0
locker = threading.Lock()  # создали объект блокировщика
# заблокировать и разблокировать область может любой поток (даже основной)
# locker = threading.RLock() также блокировщик, но область может разблокировать только тот поток,
# который ее заблокировал

def inc_value():
    global value
    while True:
        locker.acquire()  # блокируем доступ остальным потокам к данной области
        value += 1
        time.sleep(0.1)
        print(value)
        locker.release()  # освобождаем данную область и поток, который первым вызовет данный метод
        # получит доступ к данной области
    # более короткая запись блокировщика через with
    '''while True:
        with locker:
            value += 1
            time.sleep(0.1)
            print(value)'''


for _ in range(5):
    threading.Thread(target=inc_value).start()
