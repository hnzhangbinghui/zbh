# -*- coding: utf-8 -*-
import httpx
import requests
from time import sleep
import json
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

# 获取当前日期和时间
now = datetime.now()
# 获取当前日期
current_date = now.date()

url="http://www.yichayipin.com/a/11143.html"
url2="https://www.xz577.com/a/list_191_1.html"


def pachong(url):
    '''
    根据url，得到页面的数据并返回；
    :param url:
    :return:
    '''
    resp = httpx.get(url)
    bs = BeautifulSoup(resp.content, "html.parser")
    # print(bs)
    # bs1 = bs.findAll('h2', {'class': 'f-18 txt-ov mb10'})
    tag = bs.find('h2', attrs={'class': 'f-18 txt-ov mb10'})
    # print(tag)
    # print(type(tag))
    # print(len(tag))
    # print(tag.get('class'))
    t = bs.find_all('a', attrs={'class': 'fl i150 mr15'})
    return t


def save_excel(t):
    '''
    解析爬虫返回的内网，保存到txt文件和excel表；
    :param t:
    :return:
    '''
    l = []
    a = []
    b = []
    for i in range(len(t)):
        # print(t[i])
        print(t[i].get('title'), 'https://www.xz577.com' + t[i].get("href"))
        name = t[i].get('title')
        lianjie = t[i].get("href")
        # name = t[i].get('title').encode('utf-8')
        lianjie = str('https://www.xz577.com' + t[i].get("href"))
        pachong_path = r'C:\Users\zhangbinghui\Desktop\爬虫下载图片'
        l.append(name)
        a.append(lianjie)
        b.append(i + 1)
        w_path = pachong_path + '\%s.xlsx' % current_date
        # 创建一个pd.ExcelWriter对象，指定要创建的Excel文件的路径：
        excel_writer = pd.ExcelWriter('path_to_file.xlsx')
        write = pd.ExcelWriter(w_path)
        # 以列的形式进行导入数据,并写入多个sheet，参考：https://www.cnblogs.com/liupengpengg/p/12362138.html
        sheet1 = pd.DataFrame({"序号": b, "标题": l, "链接": a})
        sheet2 = pd.DataFrame({"序号2": b, "标题2": l, "链接2": a})
        sheet1.to_excel(write, sheet_name="测试1", startcol=0, index=False)
        sheet2.to_excel(write, sheet_name="测试2", startcol=0, index=False)
        with open(pachong_path + "\\标题.txt", 'a', encoding='utf-8') as f:
            f.write(t[i].get('title') + '  ' * 10 + str(lianjie) + '\n')
        # 将缓存写入工作表；
        write.save()




save_excel(pachong(url2))

























