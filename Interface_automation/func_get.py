# -*- coding= utf-8 -*-
# @Time: 2024-02-22 15:17
# @Author： Zbh


import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/85.0.4183.83 Safari/537.36'}


def api_get(url,headers=headers):
    rep=requests.get(url=url,headers=headers)
    # assert rep.status_code == 200
    return rep.status_code


