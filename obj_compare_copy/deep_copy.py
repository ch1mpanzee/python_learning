# 深度拷贝，是指重新分配一块内存，创建一个新的对象，
# 并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。
# 因此，新对象和原对象没有任何关联。

# 深拷贝只有一种形式:
# copy 模块中的 deepcopy()函数
import copy
l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)

print('l1 returns {}'.format(l1))
print('l2 returns {}'.format(l2))

# 如果被拷贝对象中存在指向自身的引用，那么程序很容易陷入无限循环：
# FIXME 不理解
# 列表 x 中有指向自身的引用，因此 x 是一个无限嵌套的列表。但是我们发现深度拷贝 x 到 y 后，程序并没有出现 stack overflow 的现象。这是为什么呢？
# 其实，这是因为深度拷贝函数 deepcopy 中会维护一个字典，记录已经拷贝的对象与其 ID。拷贝过程中，如果字典里已经存储了将要拷贝的对象，则会从字典直接返回
import copy
x = [1]
x.append(x)

print('x returns {}'.format(x))

y = copy.deepcopy(x)
print('y returns {}'.format(y))

# 思考题
# 当我们用等于操作符'=='进行比较时，输出会是什么呢？
print('x == y returns {}'.format(x == y))
# 答案
# 程序会报错：'RecursionError: maximum recursion depth exceeded in comparison'。
# 因为x是一个无限嵌套的列表，y深度拷贝x也是一个无限嵌套的列表，理论上x==y应该返回True，
# 但是x==y内部执行是会递归遍历列表x和y中每一个元素的值，由于x和y是无限嵌套的，因此会stack overflow，报错

# x.append(x)为什么会产生无限嵌套的列表呢？
# 一开始x只有一个元素，[1]，调用append方法时，长度会加1，并准备将新元素写入，x变成[1, [新元素]]，
# 但这个新元素是x自身，x现在已经是[1, [新元素]]，于是你把x放到第一个新元素的位置，
# x就从[1, [新元素] ] 就变成了[1, [1, [新元素]]]，此时新元素指向的依然是x，所以总会有个新元素。