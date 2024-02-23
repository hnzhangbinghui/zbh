# -*- coding= utf-8 -*-
# @Time: 2024-02-22 15:17
# @Author： Zbh


import requests
from zbh.Interface_automation import func_get,func_post,func_read_csv

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}


def test_api():
    result=[]
    result_dict={}
    for i in range(len(func_read_csv.read_csv())):
        if func_read_csv.read_csv()[i]['Method'] == 'post':
            a=func_post.api_post(func_read_csv.read_csv()[i]['Url'], eval(func_read_csv.read_csv()[i]['Param']), headers=headers)
            # print('返回状态：',a)
            # print(eval(func_read_csv.read_csv()[i]['Param']),type(eval(func_read_csv.read_csv()[i]['Param'])))
            # assert str(a) == func_read_csv.read_csv()[i]['Assert_code']
            if str(a) == func_read_csv.read_csv()[i]['Assert_code']:
                result_dict[func_read_csv.read_csv()[i]['describe']] = "测试通过"
            else:
                result_dict[func_read_csv.read_csv()[i]['describe']] = "测试失败"
            print("测试通过")
        else:
            a=func_get.api_get(func_read_csv.read_csv()[i]['Url'])
            # print('返回状态：', b)
            # print(func_read_csv.read_csv()[i]['Url'], func_read_csv.read_csv()[i]['Param'])
            # assert str(b) == func_read_csv.read_csv()[i]['Assert_code']
            if str(a) == func_read_csv.read_csv()[i]['Assert_code']:
                result_dict[func_read_csv.read_csv()[i]['describe']] = "测试通过"
            else:
                result_dict[func_read_csv.read_csv()[i]['describe']] = "测试失败"
            print("测试通过")
    result.append(result_dict)
    print(result)


test_api()













