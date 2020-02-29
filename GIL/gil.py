# 一、CPython引进GIL的主要原因是：
# 1. 设计者为了规避类似内存管理这样的复杂竞争风险问题（race condition）；
# 2. CPython大量使用C语言库，但大部分C语言库都不是线程安全的（线程安全会降低性能和增加复杂度）。

# 二、绕过GIL的两种思路：
# 1. 绕过CPython，使用JPython等别的实现；
# 2. 把关键性能代码放到其他语言中实现，比如C++。



import time

def CountDown(n):
    if (n>0):
        n -= 1

start_time = time.perf_counter()
CountDown(100000000)
end_time = time.perf_counter() 
print('Count Down takes {} seconds'.format(end_time - start_time))



from threading import Thread

n = 100000000
start_time = time.perf_counter()
t1 = Thread(target=CountDown, args=[n // 2])
t2 = Thread(target=CountDown, args=[n // 2])
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.perf_counter() 
print('Multi threads takes {} seconds'.format(end_time - start_time))

