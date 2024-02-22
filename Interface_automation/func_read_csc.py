# -*- coding= utf-8 -*-
# @Time: 2024-02-22 15:17
# @Author： Zbh
# @url:https://blog.csdn.net/2301_77645834/article/details/135561022

import csv
import json
import requests
import time

csv_path=r'C:\Users\zhangbinghui\PycharmProjects\zbh\Interface_automation\api_data_test.csv'


def read_csv():
    datas=[]
    try:
        with open(csv_path,'r') as cf:
            reader=csv.DictReader(cf)
            for row in reader:
                dict_data={}
                dict_data['Id']=row['Id']
                dict_data['Methon']=row['Methon']
                dict_data['Url']=row['Url']
                dict_data['Param']=row['Param']
                dict_data['Assert_code']=row['Assert_code']
                datas.append(dict_data)
    except FileExistsError:
        print("文件不存在",csv_path)

    return datas

print(read_csv())
















