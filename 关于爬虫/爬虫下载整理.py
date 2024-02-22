# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:24:26 2021

@author: zhangbinghui
"""

from urllib.request import urlretrieve
import random
import os

url = 'https://covers.zlibcdn2.com/covers299/books/b2/81/ba/b281ba3573ba1ea43bd718190b951c93.jpg'

file_name = url.split('/')[-1]
name = file_name.split('.')[0]
new_name = name + '_' + str(random.randint(1, 1000))
full_name = new_name + '.' + file_name.split('.')[-1]
file_path = os.path.dirname(__file__)
print(file_path + '/' + full_name)
# 1、通过urlretrieve方法下载；
# urlretrieve(url,filename=file_path+'/'+full_name)

# 2、通过request download下载

# import requests
# image_url='https://covers.zlibcdn2.com/covers299/books/b2/81/ba/b281ba3573ba1ea43bd718190b951c93.jpg'
# r = requests.get(image_url)
# with open(file_path+'/'+full_name,'wb') as f:
#     f.write(r.content)

'''
with open的使用格式：
with open('文件名'，'读写方式') as f:
    f.read(),#读取整个文件
    f.readline(),#读取第一行；
    f.readlines(),#读取每一行，可以结合for使用；
    f.close(),#关闭文件，文件使用完毕后要关闭，因为文件对象会占用操作系统的资源，
        并且操作系统同一时间能打开的文件数量是有限的；
    f.write(),#写入文件
    注意：带方法都要带括号，不然返回的是内存地址；
'''

# 3、视频文件，大型文件下载，可以设置每次存储文件的大小，大小文件均可下载；

import requests

image_url = 'https://p0.ssl.qhimg.com/t01e890e06c93018fa8.jpg'
# stream=True，开启时时续续的下载方式
r = requests.get(image_url, stream=True)
with open(file_path + '/' + full_name, 'wb') as f:
    # 设置每次下载文件大小
    for chunk in r.iter_content(chunk_size=32):
        # 每一次循环存储一次下载下来的内容
        f.write(chunk)
