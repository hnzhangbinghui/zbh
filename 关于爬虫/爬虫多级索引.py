'''
（注意）多级索引： 因为很多网站的HTML的属性都是比较冗余的，无法一次精确就查找到元素，
    通过逐步索引我们可以缩小我们的抖索范围，达到精确索引的目的；
1、div=html.find_all('div',di='nv')
    可以通过 .contents[1],方法付找到对应的标签，如果通过第一个索引找不到，可以通过其他的试一下，可能原因是存在一些看不见的元素
    随机应变，哈哈哈；可以直接print(div[0].contents[3])
2、可以通过逐步逐级寻找当前标签下的下级标签；print(div[0].contents[3].contents[1]) #ul下的第二个li；
    举例：print(div[0].contents[3].contents[1].contents[0])#ul下的第二个li下的第一个内容即<a>标签及其内容
3、得到标签内容可以通过 .text,获得链接内容 。get('href')或者通过索引['href']
4、

'''

import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
url = 'http://www.ihain.cn/forum.php'
head_url = 'http://www.ihain.cn/'
import random

def download_book(url):
    os.makedirs('./book/', exist_ok=True)
    header = {
        'Accept-Encodin': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

    }
    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    div=soup.find_all('div',id="category_3")
    # print(div[0].contents[1])
    for a in div:
        a.find_all('a')
        print(a.contents[1])

download_book(url)



















