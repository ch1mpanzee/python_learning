import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup

now = lambda: time.perf_counter()

async def fetchHtmlText(url):
    async with aiohttp.ClientSession(
        headers={'users-agent':'Mozilla/5.0'},
        connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    html = await fetchHtmlText(url)
    soup = BeautifulSoup(html, "html.parser")

    divs = soup.find_all('div', class_='item mod')
    urls = list(map(lambda x: x.a.img['src'], divs))
    names = list(map(lambda x: x.h3.a.string, divs))
    dats = list(map(lambda x: x.ul.li.string, divs))

    lis = zip(names, dats, urls)
    for i in lis:
        print("{0:{3}^25} \t {1:{3}^10} \t {2:{3}^}".format(i[0], i[1], i[2],chr(12288)))


start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Wall time: {}".format(now() - start))

# start_time = time.perf_counter()
# main()
# end_time = time.perf_counter()
# print('Crawl in {} seconds'.format(end_time - start_time))
