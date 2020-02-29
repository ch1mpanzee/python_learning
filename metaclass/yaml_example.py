import yaml

class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'
  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks
  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,      
       self.attacks)

yaml.load_all("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
""")

Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

print(yaml.dump(Monster(
    name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT'])))

# 输出
# !Monster
# ac: 16
# attacks: [BITE, HURT]
# hp: [3, 6]
# name: Cave lizard


# YAMLObject 的特异功能体现在哪里呢？
# 调用统一的 yaml.load_all()，就能把任意一个 yaml 序列载入成一个 Python Object；
# 调用统一的 yaml.dump()，就能把一个 YAMLObject 子类序列化。
# 对于 load_all() 和 dump() 的使用者来说，他们完全不需要提前知道任何类型信息，这让超动态配置编程成了可能。


# 我们需要一个全局的注册器，让 YAML 知道，序列化文本中的 !Monster 需要载入成 Monster 这个 Python 类型。
# 一个很自然的想法就是，那我们建立一个全局变量叫 registry，把所有需要逆序列化的 YAMLObject，都注册进去。
# 
registry = {}

def add_constructor(target_class):
    registry[target_class.yaml_tag] = target_class

# 然后，在 Monster 类定义后面加上下面这行代码：
# 
add_constructor(Monster)

# 但这样的缺点也很明显，对于 YAML 的使用者来说，每一个 YAML 的可逆序列化的类 Foo 定义后，都需要加上一句话，add_constructor(Foo)。
# 这无疑给开发者增加了麻烦，也更容易出错，毕竟开发者很容易忘了这一点。那么，更优的实现方式是什么样呢？如果你看过 YAML 的源码，就会发现，正是 metaclass 解决了这个问题。
# 

# Python 2/3 相同部分
class YAMLObjectMetaclass(type):
  def __init__(cls, name, bases, kwds):
    super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
    if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
      cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
  # 省略其余定义

# Python 3
class YAMLObject(metaclass=YAMLObjectMetaclass):
  yaml_loader = Loader
  # 省略其余定义

# Python 2
class YAMLObject(object):
  __metaclass__ = YAMLObjectMetaclass
  yaml_loader = Loader
  # 省略其余定义

# 你可以发现，YAMLObject 把 metaclass 都声明成了 YAMLObjectMetaclass，尽管声明方式在 Python 2 和 3 中略有不同。
# 在 YAMLObjectMetaclass 中， 下面这行代码就是魔法发生的地方：
cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml) 
# YAML 应用 metaclass，拦截了所有 YAMLObject 子类的定义。
# 也就是说，在你定义任何 YAMLObject 子类时，Python 会强行插入运行下面这段代码，把我们之前想要的add_constructor(Foo)给自动加上。
cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
# 所以 YAML 的使用者，无需自己去手写add_constructor(Foo) 。