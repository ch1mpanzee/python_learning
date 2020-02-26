import sys

def is_iterable(param):
    try:
        iter(param)
        return True
    except:
        return False


params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable: {}'.format(param, is_iterable(param)))


iterator_1 = [i for i in range(1000)]
generator_1 = (i for i in range(1000))

print(iterator_1)
# 生成器调用next()时，才会生成下一个元素
print(next(generator_1))
print(next(generator_1))

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式
# 迭代器可以记住遍历的位置，它有两个方法：iter() 和 next()
l1 = [1, 2, 3, 4]
iter1 = iter(l1)  # 创建迭代器对象
print(next(iter1))  # 输出迭代器的第一个元素
print(next(iter1))

# 用for语句对迭代器对象进行遍历
iter2 = iter(l1)
for i in iter2:
    print(i, end='')

# 用next()对迭代器对象进行遍历
iter3 = iter(l1)
while True:
    try:
        print(next(iter3))
    except StopIteration:
        # 调用后会引发SystemExit异常
        sys.exit(0)

# 创建一个迭代器
class myNumbers():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


Numbers = myNumbers()
NumIter = iter(Numbers)

for i in NumIter:
    print(i)


# 创建一个生成器 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1

f = fibonacci(10)  # f是生成器返回的一个迭代器对象
for i in f:
    print(i, end=" ")

# 生成器是一个返回迭代器的函数
# 在python中，使用了yield的函数被称为generator
# 执行生成器时，每次遇到yield函数会暂停并返回yield的值,下次调用next()的时候再从当前位置继续执行