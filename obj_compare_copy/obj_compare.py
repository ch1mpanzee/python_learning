# 比较操作符
# '=='表示比较对象间的值是否相等
a = 10
b = 10
print('a == b is {}'.format(a == b))

# 'is'表示比较对象是否指向同一个内存地址
print('a is b is {}'.format(a is b))

# 在 Python 中，每个对象的身份标识，都能通过函数 id(object) 获得。
# 因此，'is'操作符，相当于比较对象之间的 ID 是否相等
print('id(a) is {}'.format(id(a)))
print('id(b) is {}'.format(id(b)))
print('id(a) == id(b) is {}'.format(id(a) == id(b)))

# 对于整型数字来说，以上 a is b 为 True 的结论，只适用于 -5 到 256 范围内的数字
# Python 内部会对 -5 到 256 的整型维持一个数组，起到一个缓存的作用。
# 这样，每次你试图创建一个 -5 到 256 范围内的整型数字时，Python 都会从这个数组中返回相对应的引用，而不是重新开辟一块新的内存空间。
# 但是，如果整型数字超过了这个范围，比如上述例子中的 257，Python 则会为两个 257 开辟两块内存区域，因此 a 和 b 的 ID 不一样，a is b就会返回 False 了。
c = 257
d = 257
print('id(c) == id(d) is {}'.format(id(c) == id(d)))
# 在python解释器中使用id查看确实内存地址不同，但是使用vs code同样也是python解释器，内存地址是相同的。
# 在vscode中运行这段代码是属于同一个代码块，如果对代码块的概念不太了解可以去网上查一下。Python出于对性能的考虑，但凡是不可变对象，在同一个代码块中的对象，只有是值相同的对象，就不会重复创建，而是直接引用已经存在的对象

# 当我们比较一个变量与一个单例（singleton）时，通常会使用'is'
e , f = [], []
if e is None:
    pass
if f is not None:
    pass

# 'is'效率优于'=='
# 执行'is',就仅仅是比较两个变量的 ID 而已。
# 执行'==',相当于是去执行a.__eq__(b)，而 Python 大部分的数据类型都会去重载__eq__这个函数,其内部的处理通常会复杂一些。比如，对于列表，__eq__函数会去遍历列表中的元素，比较它们的顺序和值是否相等。


# 对于不可变（immutable）的变量, 用'is'或者'=='操作符取得的结果, 可能会变
t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print('t1 == t2 returns {}'.format(t1 == t2))

t1[-1].append(5)
print('t1 == t2 returns {}'.format(t1 == t2))



