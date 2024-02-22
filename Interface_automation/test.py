import csv

import json

import requests

import time

import unittest


def readCSV(self, filename):
    '''
    :param filename: 需要读取的数据文件
    :return: [{data1},{data2}...]
    '''

    datas = []

    try:

    # 以DictReader的方式读取数据文件，方便与json互做转换

    with open(filename, 'r') as csvfile:

    # 从文件里读取到的数据转换成字典列表的格式

    reader = csv.DictReader(csvfile)

    for row in reader:

    data = {}

    data['id'] = row['id']

    data['url'] = row['url']

    data['token'] = str(row['token'])

    data['mobile'] = row['mobile']

    data['email'] = row['email']

    data['expect'] = json.dumps(row['expect'])
        if isinstance(row['expect'], dict) \
 \
        else row['expect']  # 如果expect读取出来的不是json则取其原值，否则转为json格式保存到result里

    datas.append(data)

    return datas

    # 如果文件找不到，返回空的datas

    except FileNotFoundError:

    print("文件不存在", filename)

    return datas


