# Python 的参数传递是赋值传递 （pass by assignment）
# 让新变量与原变量指向相同的对象

# 不可变对象
def func1(b):
    b = 2
    return b

a = 1
a = func1(a)
print('a returns {}'.format(a))


# 可变对象
def my_func2(l2):
    l2.append(4)

l1 = [1, 2, 3]
my_func2(l1)
print('l1 returns {}'.format(l1))


# l4 = l4 + [4]，表示创建了一个“末尾加入元素 4“的新列表，并让 l2 指向这个新的对象。
# 这个过程与 l3 无关，因此 l3 的值不变。
def my_func4(l4):
    l4 = l4 + [4]

l3 = [1, 2, 3]
my_func4(l3)
print('l3 returns {}'.format(l3))


# 如果要改变 l3 的值，我们就得让上述函数返回一个新列表，再赋予 l3 即可：
def my_func5(l4):
    l4 = l4 + [4]
    return l4

l3 = [1, 2, 3]
l3 = my_func5(l3)
print('l3 returns {}'.format(l3))
