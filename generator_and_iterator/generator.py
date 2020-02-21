# (1 + 2 + 3 + ... + n)^2 = 1^3 + 2^3 + 3^3 + ... + n^3

def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

def get_sum(n):
    sum1, sum3 = 0, 0
    gen1 = generator(3)
    for i in range(1, n+1):
        sum3 += next(gen1)
        sum1 += i
    print(sum1*sum1, sum3)

get_sum(8)


# 给定一个 list 和一个指定数字，求这个数字在 list 中的位置。

# 普通方法
l1 = [1,2,3,4,6,2,10,2,8,7]
def normal_index(target,l1):
    l2 = []
    for index, item in enumerate(l1):
        if target == item:
            l2.append(index)
    return l2

print(normal_index(2,l1))

# 使用生成器
def index_generator(target,l1):
    for index, item in enumerate(l1):
        if target == item:
            yield index
            print(1)

# 不明白为什么此处不调用next()也能遍历，理解出错了！
# 误以为生成器必须和next()搭配使用，其实是和yield配合使用
# 迭代器的遍历可以用for语句，也可以用next()

# 此处index_generator(2,l1)作为一个迭代器对象，使用 list 转换为列表后，才能用 print 输出。
print(list(index_generator(2,l1)))

