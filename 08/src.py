# 错误：语法错误，无法被执行
# 异常：执行过程中抛出异常

# handle exception
import sys

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())

except ValueError as err:
    print('Value Error: {}'.format(err))

print('continue')


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except (ValueError, IndexError) as err:
    print('Error: {}'.format(err))

print('continue')


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))

print('continue')


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))

print('continue')


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    ...
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')

print('continue')


try:
    f = open('file.txt', 'r')
    # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()


# 用户自定义异常
class MyInputError(Exception):
    """Exception raised when there're errors in input"""

    def __init__(self, value):
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)
except MyInputError as err:
    print('error:{}'.format(err))

# 以数据库的连接、读取为例，下面两种写法，你觉得哪种更好呢？

try:
    db = DB.connect('<db path>')  # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>')  # 可能会抛出异常
except (DBConnectionError, DBQueryDataError) as err:
    print('Error: {}'.format(err))

# 第二种

try:
    db = DB.connect('<db path>')  # 可能会抛出异常
    try:
        raw_data = DB.queryData('<viewer_id>')
    except DBQueryDataError as err:
        print('DB query data error: {}'.format(err))
except DBConnectionError as err:
    print('DB connection error: {}'.format(err))

# 第一种写法更加简洁，易于阅读。而且except后面的错误类型先抛出数据库连接错误，之后才抛出查询错误，实现的异常处理和第二种一样。


e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    pass

print(e)  # NameError: name 'e' is not defined

# "When an exception has been assigned using as target, it is cleared at the end of the except clause."
except E as N:
    foo

# 就等于
except E as N:
    try:
        foo
    finally:
        del N

# 因此例子中的e最后被delete了，所以会抛出NameError
