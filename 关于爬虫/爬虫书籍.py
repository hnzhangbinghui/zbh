import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url='https://zh.ng1lib.org/book/5499203/ac60de?dsource=mostpopular'

import random
def download_book(url):
    os.makedirs('./book/',exist_ok=True)
    header = {
        'Accept-Encodin': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

    }
    html=requests.get(url,headers=header).text
    soup=BeautifulSoup(html,'html.parser')
    div=soup.find_all('div')
    # print(div)
    for d in div:
        if len(d.find_all('a'))==0:
            pass
        else:
            a=d.find_all('a')
            for i in range(len(a)):
                if a[i]['href'].find('https') & a[i]['href'].find('.jpg'):
                    pass
                else:
                    # print(a[i]['href'])
                    # urlretrieve(a[i]['href'],os.getcwd()+'/'+str(random.randint(1,100))+'.jpg')
                    print(a[i]['href'])



    # for i in range(len(div)):
    #     print(div[i])
    #     if div[i]['src'].find('http'):
    #         pass
    #     else:
    #         urlretrieve(div[i]['src'],os.getcwd()+'/'+str(random.randint(1,100))+'.jpg')
    #         print(div[i]['src'])
















download_book(url)























