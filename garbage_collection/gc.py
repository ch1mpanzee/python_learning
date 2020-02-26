# python中的GC的策略：
# 1. 引用计数机制为主
# 2. 标记-清除和分代收集两种机制为辅


# 计数引用：当一个对象的引用次数为0的时候，说明这个对象永不可达，将会被作为垃圾回收
import gc
import sys
import os
import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 2014. / 2014
    print('{} memory used: {} MB'.format(hint, memory))


# 函数func()内部声明的列表 a 是局部变量，在函数返回后，局部变量的引用会注销掉
def func1():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

func1()
show_memory_info('finished')


# global b 表示将 b 声明为全局变量。那么，即使函数返回后，列表的引用依然存在，于是对象就不会被垃圾回收掉，依然占用大量内存。
def func2():
    show_memory_info('initial')
    global b
    b = [i for i in range(10000000)]
    show_memory_info('after b created')


func2()
show_memory_info('finished')


# 如果我们把生成的列表返回，然后在主程序中接收，那么引用依然存在，垃圾回收就不会被触发，大量内存仍然被占用着：
def func3():
    show_memory_info('initial')
    c = [i for i in range(10000000)]
    show_memory_info('after c created')
    return c

c = func3()
show_memory_info('finished')


# Python 内部的引用计数机制
# sys.getrefcount() 这个函数，可以查看一个变量的引用次数。
# getrefcount 本身也会引入一次计数。
# 在函数调用发生的时候，会产生额外的两次引用，一次来自函数栈，另一个是函数参数。

d = []
# 2次引用，一次来自 d ,一次来自 getrefcount
print(sys.getrefcount(d))


def func4(d):
    # 4次引用，d，python 的函数调用栈，函数参数，和 getrefcount(当前这一次的getrefcount,之前执行的已经不存在)
    print(sys.getrefcount(d))


func4(d)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(d))


# 手动释放内存
# 先调用 del a 来删除对象的引用；然后强制调用 gc.collect()，清除没有引用的对象

show_memory_info('initial')
e = [i for i in range(10000000)]
show_memory_info('after e created')

del e
gc.collect()
show_memory_info('finished')
# print(e)


# 循环引用
# 可以显式调用 gc.collect() ，来启动垃圾回收。
def func5():
    show_memory_info('initial')
    f = [i for i in range(10000000)]
    g = [i for i in range(10000000)]
    show_memory_info('after f, g created')
    f.append(g)
    g.append(f)

func5()
gc.collect()
show_memory_info('finished')


# 标记清除（mark-sweep）算法
# 先用图论来理解不可达的概念。
# 对于一个有向图，如果从一个节点出发进行遍历，并标记其经过的所有节点；
# 那么，在遍历结束后，所有没有被标记的节点，我们就称之为不可达节点。
# 显而易见，这些节点的存在是没有任何意义的，自然的，我们就需要对它们进行垃圾回收。
# 当然，每次都遍历全图，对于 Python 而言是一种巨大的性能浪费。
# 所以，在 Python 的垃圾回收实现中，mark-sweep 使用双向链表维护了一个数据结构，并且只考虑容器类的对象（只有容器类对象才有可能产生循环引用）


# 分代收集（generational）算法
# Python 将所有对象分为三代。
# 刚刚创立的对象是第 0 代；经过一次垃圾回收后，依然存在的对象，便会依次从上一代挪到下一代。
# 而每一代启动自动垃圾回收的阈值，则是可以单独指定的。
# 当垃圾回收器中新增对象减去删除对象达到相应的阈值时，就会对这一代对象启动垃圾回收。
# 分代收集基于的思想是，新生的对象更有可能被垃圾回收，而存活更久的对象也有更高的概率继续存活。


# 调试内存泄漏方面， objgraph 是很好的可视化分析工具，一个可视化引用关系的包。
# show_refs()，它可以生成清晰的引用关系图。

import objgraph

h = [1, 2, 3]
i = [4, 5, 6]

h.append(i)
i.append(h)

objgraph.show_refs([h])
objgraph.show_backrefs([h])