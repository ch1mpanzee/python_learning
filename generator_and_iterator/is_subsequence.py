# 给定两个序列，判定第一个是不是第二个的子序列。

# greedy algorithm


def greedy(sub_string, string):
    if len(sub_string) <= 0:
        return "substring is null"
    if len(string) <= 0:
        return "string is null"
    index1, index2 = 0, 0
    for i in string:
        if sub_string[index1] == i:
            index1 += 1
        index2 += 1
        if index1 == len(sub_string):
            return True
    return False


print(greedy('abcd', 'abc'))

# 迭代器方法

# (i in b) 等价于下列代码

# while True:
#     var = next(b)
#     if var == i:
#         yield True

gen = (i for i in range(5))

print(2 in gen)
print(4 in gen)
print(3 in gen)

# 用生成器实现is_subsequence方法

sub_string = 'bca'
string = 'abc'

def is_subsequence(sub_string, string):
    string = iter(string)  # 这句话如果不写貌似也是正确的，为什么？
    return all((i in string) for i in sub_string)

print('{} is a subsequence of {}: {}'.format(sub_string, string, is_subsequence(sub_string, string)))

# 如果不把string转换成一个迭代器对象，则（i in string)不会按序判断
def is_subsequence_wrong(sub_string, string):
    # string = iter(string)  # 注释掉这句话
    return all((i in string) for i in sub_string)

print('{} is a subsequence of {}: {}'.format(sub_string, string, is_subsequence_wrong(sub_string, string)))


test=[2, 4, 3]
print(2 in test)
print(3 in test)
print(4 in test)
