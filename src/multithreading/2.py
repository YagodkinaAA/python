import time
import threading


def get_data(data, value):  # value-значение, которое будет использоваться в иттерациях, data-данные,которые будем передавать
    for _ in range(value):
        print(f'[{threading.current_thread().name}] - {data}')  # threading.current_thread().name-получили
        # из текщего потока параметр name
        time.sleep(1)


# создаем список, в котором будем хранить объекты всех потоков
thr_list = []

# создаем 3 потока
for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,),
                           name=f'thr-{i}')  # target-адрес функции, скобки не ставили,
    # чтоб был именно адрес, args принимает кортеж, поэтому запятая (args-аргументы,
    # которые пердаем в функцию)
    thr_list.append(thr)
    thr.start()  # запускаем поток

#print(thr_list)

for i in thr_list:
    i.join()  # ждем выполнения потока, затем переходим на следующий,
    # только когда все потоки выполнятся, мы попадем на следующую строчку кода

print('finish!')

