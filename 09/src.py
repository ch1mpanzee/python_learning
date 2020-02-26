
# 不能在函数内部随意改变全局变量的值，Python 的解释器会默认函数内部的变量为局部变量

MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    MIN_VALUE += 1

validation_check(5)

# 如果我们一定要在函数内部改变全局变量的值，就必须加上 global 这个声明：

MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    global MIN_VALUE
    MIN_VALUE += 1

validation_check(5)

# 如果遇到函数内部局部变量和全局变量同名的情况，那么在函数内部，局部变量会覆盖全局变量

MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    MIN_VALUE = 3

# 对于嵌套函数来说，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上 nonlocal 这个关键字：

def outer():
    x = "local"
    def inner():
        nonlocal x # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 输出
inner: nonlocal
outer: nonlocal

# 如果不加上 nonlocal 这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。

def outer():
    x = "local"
    def inner():
        x = 'nonlocal' # 这里的x是inner这个函数的局部变量
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 输出
inner: nonlocal
outer: local



# 嵌套函数
# 使用递归的方式计算一个数的阶乘。
# 因为在计算之前，需要检查输入是否合法，所以我写成了函数嵌套的形式，这样一来，输入是否合法就只用检查一次。
# 而如果我们不使用函数嵌套，那么每调用一次递归便会检查一次，这是没有必要的，也会降低程序的运行效率。

def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)


print(factorial(5))


# 闭包closure
# 闭包其实和刚刚讲的嵌套函数类似，不同的是，这里外部函数返回的是一个函数，而不是一个具体的值。返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用。

# 计算一个数的 n 次幂，用闭包可以写成下面的代码：

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是exponent_of函数

square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方 
square
# 输出
<function __main__.nth_power.<locals>.exponent(base)>

cube
# 输出
<function __main__.nth_power.<locals>.exponent(base)>

print(square(2))  # 计算2的平方
print(cube(2)) # 计算2的立方
# 输出
4 # 2^2
8 # 2^3

# 使用闭包的一个原因，是让程序变得更简洁易读

def nth_power_rewrite(base, exponent):
    return base ** exponent


# 不使用闭包
res1 = nth_power_rewrite(base1, 2)
res2 = nth_power_rewrite(base2, 2)
res3 = nth_power_rewrite(base3, 2)
...

# 使用闭包
square = nth_power(2)
res1 = square(base1)
res2 = square(base2)
res3 = square(base3)
...

# 闭包常常和装饰器（decorator）一起使用