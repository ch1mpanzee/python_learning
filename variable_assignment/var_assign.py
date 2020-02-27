# 在Python中, 变量的赋值表示让变量指向了某一个对象，而不是把对象拷贝给变量
# 一个对象可以被多个变量指向

# 对于不可变对象，比如数字,字符串,元组,不可变集合
i1 = 10
i2 = i1
print('id(i1) == id(i2) returns {}'.format(id(i1) == id(i2)))
# 通过某些操作（+= 等等）更新不可变对象的值时，会返回一个新的对象。
i1 += 1
print('id(i1) == id(i2) returns {}'.format(id(i1) == id(i2)))


# FIXME 集合到底是可变还是不可变


# 对于可变对象, 比如列表，字典，集合等等
l1 = [1,2,3]
l2 = l1
print('id(l1) == id(l2) returns {}'.format(id(l1) == id(l2)))
# 可变对象的改变，会影响所有指向该对象的变量
l1.append(4)
print('l1 returns {}'.format(l1))
print('l2 returns {}'.format(l2))
print('id(l1) == id(l2) returns {}'.format(id(l1) == id(l2)))

# 变量可以被删除，但是对象无法被删除
del l2