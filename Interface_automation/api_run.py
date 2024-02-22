# -*- coding= utf-8 -*-
# @Time: 2024-02-22 15:17
# @Author： Zbh


import requests
from zbh.Interface_automation import func_get,func_post,func_read_csc


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/85.0.4183.83 Safari/537.36'}
# url='http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin'
#
# res_data={
#     'loginName':'ab',
#     'password':'Ysstech123!@#',
#     'validType':0}
# url2='http://192.168.99.158:9080/acp-custody/rest/login/extend/findAllImgInfo?token=null&count=0&_=1708589683270'

# func_get.api_get(url2)
# func_post.api_post(url,res_data)


def test_api():
    for i in range(len(func_read_csc.read_csv())):
        if func_read_csc.read_csv()[i]['Methon'] == 'post':
            a=func_post.api_post(func_read_csc.read_csv()[i]['Url'],func_read_csc.read_csv()[i]['Param'])
            print((func_read_csc.read_csv()[i]['Url'],func_read_csc.read_csv()[i]['Param']))
            print(a)
            assert a == func_read_csc.read_csv()[i]['Assert_code']

        else:
            b=func_get.api_get(func_read_csc.read_csv()[i]['Url'])
            assert str(b)== func_read_csc.read_csv()[i]['Assert_code']


test_api()














