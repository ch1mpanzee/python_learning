l = [1, 2, "smart", True]
l[3] = False

tup = (1, "smart", 2, 3)
# tup[1] = "stupid"

l.append(5)
new_tup = tup + (5,)

l[-1]
tup[-1]

l[1:2]
tup[1:2]

l = [[1,2],[3,4]]
tup= ((11,22),(33,44))

new_l = list(tup)
new_tup = tuple(l)

l = [1,2,3,3,3,4]
print(l.index(2))
print(l.count(3))
l.reverse()
print(l)
l.sort()
print(l)
print(reversed(l))
print(sorted(l))

tup=(1,2,3,3,3,4)
print(tup.count(3))
print(tup.index(2))
print(reversed(tup))
print(sorted(tup))



l = [1, 2, 3]
print(l.__sizeof__())
tup = (1, 2, 3)
print(tup.__sizeof__())


l = []
print(l.__sizeof__()) 
# 空列表的存储空间为40字节
l.append(1)
print(l.__sizeof__()) 
# 加入了元素1之后，列表为其分配了可以存储4个元素的空间 (72 - 40)/8 = 4
l.append(2) 
print(l.__sizeof__())
# 由于之前分配了空间，所以加入元素2，列表空间不变
l.append(3)
print(l.__sizeof__()) 
# 同上
l.append(4)
print(l.__sizeof__()) 
# 同上
l.append(5)
print(l.__sizeof__()) 
# 加入元素5之后，列表的空间不足，所以又额外分配了可以存储4个元素的空间


# python3 -m timeit 'x=[1,2,3,4,5,6]'
# python3 -m timeit 'x=(1,2,3,4,5,6)'
# python3 -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
# python3 -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'


# 创建一个空的列表，A、B 两种方式，在效率上有什么区别吗？应该优先考虑使用哪种呢？
# option A
empty_list = list()

# option B
empty_list = []

# list()是一个function call，Python的function call会创建stack，并且进行一系列参数检查的操作，比较expensive，反观[]是一个内置的C函数，可以直接被调用，因此效率高。