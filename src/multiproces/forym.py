from multiprocessing import Process
import time

print(1)


def func1():
    print('test1')
    time.sleep(1)


def func2():
    print('test2')
    time.sleep(5)


def test_multiprocessing():
    if __name__ == '__main__':
        p_func1 = Process(target=func1)
        p_func2 = Process(target=func2)
        p_func1.start()
        p_func2.start()
        #p_func1.join()
        #p_func2.join()
        #print('done')
test_multiprocessing()