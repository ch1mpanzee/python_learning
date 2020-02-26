# Python线程创建的几种方法

# 1. 使用Thread类创建
import os
from concurrent.futures import ThreadPoolExecutor
import threading
import time
from time import sleep, ctime

now = lambda: time.perf_counter()

def cook():
    print('cooking: {}'.format(ctime()))
    sleep(1)


def sing():
    print('singing: {}'.format(ctime()))
    sleep(2)


def main1():
    print('start: {}'.format(ctime()))

    t1 = threading.Thread(target=cook)
    t2 = threading.Thread(target=cook)

    t1.start()
    t2.start()

    print('end: {}'.format(ctime()))

start1 =now()
main1()
print('Wall time1: {}'.format(now()-start1))


# 2. 使用Thread子类创建
# 为了让每个线程的封装性更完美，所以使用threading模块时，往往会定义一个新的子类class，只要继承threading.Thread就可以了，然后重写run方法。
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(1)
        print('i am {}'.format(self.name))


def main2():
    print('start: {}'.format(ctime()))

    t1 = MyThread('thread-1')
    t2 = MyThread('thread-2')

    t1.start()
    t2.start()

    print('end: {}'.format(ctime()))

start2 = now()
main2()
print('Wall time2: {}'.format(now()-start2))


# 3. 使用线程池ThreadPoolExecutor创建
def say_hello(name):
    sleep(1)
    print('hello {}'.format(name))


def main3():
    names = ['bob', 'mary', 'bill']
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     for name in names:
    #         executor.submit(say_hello, name)
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(say_hello, names)


start3 = now()
main3()
print("Wall time3: {}".format(now() - start3))

