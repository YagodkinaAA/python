import time
import threading

data = threading.local()  # позволяет хранить данные в потоках и задавать нужные атрибуты,
# а также задавать значения этим атрибутам

'''def get():
    print(data.value)'''

def t1():
    data.value = {'value': 1} #атрибут может принимать абсолютно любые значения (даже списки и словари)
    #get()
    print('t1:', data.value)


def t2():
    data.test = ['test1', 'test2']
    #get()
    print('t2:', data.test)


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()