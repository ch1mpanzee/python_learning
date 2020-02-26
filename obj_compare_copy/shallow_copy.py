# 浅拷贝 shallow copy
# 浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是原对象中子对象的引用

# 浅拷贝有三种形式
# 方法一: 使用数据类型本身的构造器

l1 = [1, 2, 3]
l2 = list(l1)

print('l2 returns {}'.format(l2))

print('l1 == l2 returns {}'.format(l1 == l2))

print('l1 is l2 returns {}'.format(l1 is l2))


s1 = set([1, 2, 3])
s2 = set(s1)

print('s2 returns {}'.format(s2))

print('s1 == s2 returns {}'.format(s1 == s2))

print('s1 is s2 returns {}'.format(s1 is s2))


# 方法二: 对于可变的序列，我们还可以通过切片操作符':'完成浅拷贝
l3 = [1, 2, 3, 4, 5]
l4 = l3[:]

print('l4 returns {}'.format(l4))

print('l3 == l4 returns {}'.format(l3 == l4))

print('l3 is l4 returns {}'.format(l3 is l4))


# 方法三: copy 模块中的 deepcopy()函数，适用于任何数据类型
import copy
s3 = set([1, 2, 3])
s4 = copy.copy(s3)

print('s4 returns {}'.format(s4))

print('s3 == s4 returns {}'.format(s3 == s4))

print('s3 is s4 returns {}'.format(s3 is s4))

# FIXME 记忆不深，不理解
# 需要注意的是，对于元组，使用 tuple() 或者切片操作符':'不会创建一份浅拷贝，相反，它会返回一个指向相同元组的引用：

t1 = (1, 2, 3)
t2 = tuple(t1)

print('t2 returns {}'.format(t2))

print('t1 == t2 returns {}'.format(t1 == t2))

print('t1 is t2 returns {}'.format(t1 is t2))


# 浅拷贝的副作用
# 浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是原对象中子对象的引用
# 如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会带来一些副作用

l5 = [[1, 2], (30, 40)]
l6 = list(l5)

l5.append(100)
print('l5 returns {}'.format(l5))
print('l6 returns {}'.format(l6))

l5[0].append(3)
print('l5 returns {}'.format(l5))
print('l6 returns {}'.format(l6))

# 因为元组是不可变的，这里表示对 l1 中的第二个元组拼接，然后重新创建了一个新元组作为 l1 中的第二个元素，
# 而 l2 中没有引用新元组，因此 l2 并不受影响。
l5[1] += (50, 60)
print('l5 returns {}'.format(l5))
print('l6 returns {}'.format(l6))


import copy
a = 1  # 不可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  # 内存地址相同

a = [1,2]  # 可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  # 内存地址不相同
print(id(a[0])==id(copy_a[0]))

a = ([1,2],(3,4))  # 不可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  
print(id(a[0])==id(copy_a[0]))  
print(id(a[1])==id(copy_a[1]))  

a = ((1,2),(3,4))  # 不可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  
print(id(a[0])==id(copy_a[0]))  
print(id(a[1])==id(copy_a[1]))  

a = [(1,2),[3,4]]  # 可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  
print(id(a[0])==id(copy_a[0]))  
print(id(a[1])==id(copy_a[1]))  

a = [(1,2),(3,4)]  # 可变数据类型
copy_a = copy.copy(a)
print(id(a)==id(copy_a))  
print(id(a[0])==id(copy_a[0]))  
print(id(a[1])==id(copy_a[1]))  

# 浅拷贝，如果外层是不可变对象，则原对象与拷贝对象地址相同，内部元素无论可变与否地址都相同
# 如果外层是可变对象，则原对象与拷贝对象地址不同，内部元素无论可变与否地址都相同