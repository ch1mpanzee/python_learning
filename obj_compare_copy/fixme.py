# 对于非容器类型，如数字、字符，以及其他的“原子”类型，没有拷贝一说，产生的都是原对象的引用。
# 如果元组变量值包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝。

# FIXME 记忆不深，不理解
# 需要注意的是，对于元组，使用 tuple() 或者切片操作符':'不会创建一份浅拷贝，相反，它会返回一个指向相同元组的引用：

t1 = (1, 2, 3)
t2 = tuple(t1)

print('t2 returns {}'.format(t2))

print('t1 == t2 returns {}'.format(t1 == t2))

print('t1 is t2 returns {}'.format(t1 is t2))