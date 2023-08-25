import time
import threading

data = threading.local()  # позволяет хранить данные в потоках и задавать нужные атрибуты,
# а также задавать значения этим атрибутам

def get_name():
    print(data.name)


def t1():
    data.name = threading.current_thread().name
    get_name()


def t2():
    data.name = threading.current_thread().name
    get_name()


threading.Thread(target=t1, name='t1').start()
threading.Thread(target=t2, name='t2').start()
