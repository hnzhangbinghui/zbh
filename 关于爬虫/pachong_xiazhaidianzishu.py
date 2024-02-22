# -*- coding: utf-8 -*-
import httpx
import requests
from time import sleep
import json
from bs4 import BeautifulSoup

root_url="https://www.xz577.com"
url_dianzishu="https://www.xz577.com/e/python/"
url_pdf="http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szse"


# 电子书的代码
# resp=httpx.get(url_dianzishu)
# bs=BeautifulSoup(resp.content,"html.parser")
# # print(bs)
# # bs1 = bs.findAll('h2', {'class': 'f-18 txt-ov mb10'})
# tag=bs.find_all('a',attrs={'class': 'item-app1'})
# for t in range(len(tag)):
#     shuming = tag[t].get('title')
#     # addr = root_url + tag[t].get('href')
#     addr="{}{}".format(root_url,tag[t].get('href')) #格式化字符串
#     print(shuming, addr)



# pdf


resp=httpx.get(url_pdf)
bs=BeautifulSoup(resp.content,"html.parser")
# print(bs)
tag = bs.find_all('a', {'class': 'p-hover'})
print(tag)
# for t in range(len(tag)):
#     shuming = tag[t].get('title')
#     # addr = root_url + tag[t].get('href')
#     addr="{}{}".format(root_url,tag[t].get('href')) #格式化字符串
#     print(shuming, addr)


















