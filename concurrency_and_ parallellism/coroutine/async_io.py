# asyncio是Python3.4之后引入的标准库，支持异步IO

# asyncio的模型是一个消息循环, 从asyncio模块获取一个EventLoop, 把需要执行的协程扔进EventLoop中, 就实现了异步IO。
import asyncio

# 1. 使用@asyncio.coroutine和yield from的方式实现协程
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
    yield from asyncio.sleep(1)
    print("Hello again!")

# 2. 使用async和await的方式实现协程, Python从3.5版本开始为asyncio提供了async和await的新语法
async def hello1():
    print("Hello world!")
    await asyncio.sleep(1)
    print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# HTTP连接就是IO操作, aiohttp则是基于asyncio实现的HTTP框架