# asyncio.run, asyncio.create_task 是 Python 3.7 之后才有的特性

import time


def crawl_page(url):
    print('Crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


start_time = time.perf_counter()
urls = ['url_1', 'url_2', 'url_3', 'url_4']
main(urls)
end_time = time.perf_counter()
print('Crawl {} urls in {} seconds'.format(len(urls), end_time - start_time))



import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    for url in urls:
        # await 是同步调用
        # await 执行的效果，和 Python 正常执行是一样的，也就是说程序会阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续
        await crawl_page(url)

start_time = time.perf_counter()
urls = ['url_1', 'url_2', 'url_3', 'url_4']
asyncio.run(main(urls))
end_time = time.perf_counter()
print('Crawl {} urls in {} seconds'.format(len(urls), end_time - start_time))



async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

start_time = time.perf_counter()
urls = ['url_1', 'url_2', 'url_3', 'url_4']
asyncio.run(main(urls))
end_time = time.perf_counter()
print('Crawl {} urls in {} seconds'.format(len(urls), end_time - start_time))



async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # *tasks 解包列表，将列表变成了函数的参数；与之对应的是， ** dict 将字典变成了函数的参数。
    await asyncio.gather(*tasks)

start_time = time.perf_counter()
urls = ['url_1', 'url_2', 'url_3', 'url_4']
asyncio.run(main(urls))
end_time = time.perf_counter()
print('Crawl {} urls in {} seconds'.format(len(urls), end_time - start_time))
