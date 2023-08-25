import time
import threading


def get_data(data):
    for _ in range(5):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True, name='thr')
#daemon=True-при завершеннии программы все потоки автоматически завершаются(по умолчанию стоит False)
#thr.setDaemon(True) #обратились к потоку и задали ему значение демона
thr.start()
time.sleep(1)
print('finish!')
