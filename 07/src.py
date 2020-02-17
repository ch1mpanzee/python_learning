# 条件

# y=|x|
if x < 0:
    y = -x
else:
    y = x

if id == 0:
    print('red')
elif id == 1:
    print('yellow')
else:
    print('green')

# 条件判断中除了boolean类型，条件判断最好是显性，比如str，int，obj，list/tuple/dict/set


# 循环

# Python中的数据结构只要是可迭代的（iterable）比如list，set，都可以用以下方式遍历
l = [1, 2, 3, 4]
for item in l:
    print(item)

# 字典dict只有键key是可迭代的iterable
d = {'name': 'yukiyo', 'age': 27, 'gender': 'male'}
for k in d:  # 遍历字典的键
    print(k)
for v in d.values():  # 遍历字典的值
    print(v)
for k, v in d.items():  # 遍历字典的键值对
    print('key:{} value:{}'.format(k, v))

# Python内置的函数enumerate()遍历集合，不仅可以返回每个元素还能返回对应的索引
l = [1, 2, 4, 3, 5, 6]
for index, value in enumerate(l):
    if index == 3:
        print(value)

# continue跳过当前循环，继续执行下一轮循环
# break完全跳出循环


# name_price: 产品名称(str)到价格(int)的映射字典
# name_color: 产品名字(str)到颜色(list of str)的映射字典
for name, price in name_price.items():
    if price < 1000:
        if name in name_color:
            for color in name_color[name]:
                if color != 'red':
                    print('name:{},color:{}'.format(name, color))
        else:
            print('name:{},color:{}'.format(name, None))

# 加入continue后，最多只有三层嵌套
for name, price in name_price.items():
    if price >= 1000:
        continue
    if name not in name_color:
        print('name:{},color:{}'.format(name, None))
        continue
    for color in name_color[name]:
        if color == 'red':
            continue
        print('name:{},color:{}'.format(name, color))

# while满足条件时进入循环，不满足跳出循环
while True:
    try:
        text = input('Please enter your questions, enter "q" to exit')
        if text == 'q':
            print('exit system')
            break
        print('response your question ...')
    except as err:
        print('Encountered error:{}'.format(err))
        break

# 比较while和for的效率

i = 0
while i < 1000000:
    i += 1

for i in range(0, 1000000):
    pass

# i是整型，不可变immutable，i+=1相当于i=new int(i+1)涉及对象创建和删除
# range()直接由C语言写的，调用它速度非常快


# 条件和循环做一行操作

for item in iterable:
    if condition:
        expression1
    else:
        expression2

# 等价于
expression1 if condition else expression2 for item in iterable

for item in iterable:
    if condition:
        expression1

# 等价于
expression1 for item in iterable if condition

# 绘制y=2*|x|+5的函数图像，给定集合x的数据点，计算y的数据点
y = [(2 * value + 5) if value > 0 else (-2 * value + 5) for value in x]

# 将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 5 的单词，最后返回由单词组成的列表。
text = '  good, morning,   ahhhhh  '
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 5]

# 给定两个列表 x、y，要求返回 x、y 中所有元素对组成的元祖，相等情况除外
[(xx, yy) for xx in x for yy in y if xx != yy]

# 等价于
l = []
for xx in x:
    for yy in y:
        if xx != yy:
            l.append((xx, yy))

# 给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。attributes = ['name', 'dob', 'gender']

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]

# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
 {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
 {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

[dict(zip(attributes, value)) for value in values]
