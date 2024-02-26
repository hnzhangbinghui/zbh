# -*- coding= utf-8 -*-
# @Time: 2024-02-22 15:17
# @Author： Zbh


import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}

# url="http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin"
#
# res_data={"loginName":"ab","password":"Ysstech123!@#","validType":0}


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}
url="http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin"

res_data={"loginName":"ab","password":"Ysstech123!@#","validType":0}



def api_post(url,data,headers=headers):
    '''
    :param url: 接口地址，通过csv文件获取；
    :param data: 接口的入参；
    :param headers:请求头；
    :return:
    '''
    rep = requests.post(url=url,params=data,headers=headers)
    # assert rep.status_code == 200
    return rep.status_code




# print(api_post(url,res_data))
# print(url,res_data,type(res_data))

# http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin?token=null {"loginName":"ab","password":"Ysstech123!@#","validType":0}
