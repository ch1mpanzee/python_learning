# metaclass 的底层原理

# 第一，所有的 Python 的用户定义类，都是 type 这个类的实例。

# 可能会让你惊讶，事实上，类本身不过是一个名为 type 类的实例。
# 在 Python 的类型世界里，type 这个类就是造物的上帝。这可以在代码中验证：
# Python 3和Python 2类似
class MyClass: 
    pass

instance = MyClass()
print(type(instance)) # 输出<class '__main__.MyClass'>
print(type(MyClass)) # 输出<class 'type'>
# 你可以看到，instance 是 MyClass 的实例，而 MyClass 不过是“上帝”type 的实例。


# 第二，用户自定义类，只不过是 type 类的__call__运算符重载。

# 当我们定义一个类的语句结束时，真正发生的情况，是 Python 调用 type 的__call__运算符。简单来说，当你定义一个类时，写成下面这样时：

class MyClass:
  data = 1

# Python 真正执行的是下面这段代码：
class = type(classname, superclasses, attributedict)

# 这里等号右边的type(classname, superclasses, attributedict)，就是 type 的__call__运算符重载，它会进一步调用：
type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)

# 当然，这一切都可以通过代码验证，比如下面这段代码示例：
class MyClass:
  data = 1
  
instance = MyClass()
print(MyClass, instance) # 输出 (__main__.MyClass, <__main__.MyClass instance at 0x7fe4f0b00ab8>)
print(instance.data) # 输出 1

MyClass = type('MyClass', (), {'data': 1})
instance = MyClass()
print(MyClass, instance) # 输出 (__main__.MyClass, <__main__.MyClass at 0x7fe4f0aea5d0>)
print(instance.data) # 输出 1

# 由此可见，正常的 MyClass 定义，和你手工去调用 type 运算符的结果是完全一样的。


# 第三，metaclass 是 type 的子类，通过替换 type 的__call__运算符重载机制，“超越变形”正常的类。
# 
# 其实，理解了以上几点，我们就会明白，正是 Python 的类创建机制，给了 metaclass 大展身手的机会。
# 一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的__call__运算符重载。
class = type(classname, superclasses, attributedict) 
# 变为了
class = MyMeta(classname, superclasses, attributedict)
# 所以，我们才能在上面 YAML 的例子中，利用 YAMLObjectMetaclass 的__init__方法，为所有 YAMLObject 子类偷偷执行add_constructor()。


# 使用metaclass有风险，因为深入理解的人并不多，有可能出现滥用的可能