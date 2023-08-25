import time
import threading


def get_data(data):  # thr_name-имя потока, data-данные,которые будем передавать
    while True:
        print(f'[{threading.current_thread().name}] - {data}')  # threading.current_thread().name-получили
        # из текщего потока параметр name
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),),
                       name='thr-1')  # target-адрес функции, скобки не ставили,
# чтоб был именно адрес, args принимает кортеж, поэтому запятая
thr.start()  # запускаем поток

print('name:', threading.main_thread().name) # обратились к основному потоку и вызвали атрибут имени
threading.main_thread().setName('result') # изменили имя основного потока
print('result:', threading.main_thread().name) # получаем основной поток выполнения и после точки выводим
# атрибуты данного потока, которые нас интересуют


for i in range(100):
    print(f'current:{i}')
    time.sleep(1)

    if i % 10 == 0:
        print('active thread:', threading.active_count())  # выводим кол-во активных потоков
        print('enumerate:', threading.enumerate())  # выводим все потоки, которые запущены в данный момент
        print('thr-1 is alive', thr.is_alive())  # проверяем работает ли наш поток в данный момент
