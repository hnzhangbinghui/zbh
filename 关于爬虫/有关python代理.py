# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:37:27 2021

@author: zhangbinghui
"""
'''
我们在做爬虫的过程中经常会遇到这样的情况：最初爬虫正常运行，正常抓取数据，一切看起来都是那么的美好，
然而一杯茶的功夫可能就会出现错误，比如403 Forbidden；出现这样的原因往往是网站采取了一些反爬虫的措施，
比如，服务器会检测某个IP在单位时间内的请求次数，如果超过了某个阈值，那么服务器会直接拒绝服务，返回一些错误信息。
这时候，代理就派上用场
关于爬虫原理：
1、代理实际上指的就是代理服务器，英文叫作proxy server，它的功能是代理网络用户去取得网络信息。形象地说，它是网络信息的中转站。
2、在我们正常请求一个网站时，是发送了请求给Web服务器，Web服务器把响应传回给我们。如果设置了代理服务器，实际上就是在本机和服务器之间搭建了一个桥，
3、此时本机不是直接向Web服务器发起请求，而是向代理服务器发出请求，请求会发送给代理服务器，然后由代理服务器再发送给Web服务器，
3、接着由代理服务器再把Web服务器返回的响应转发给本机。这样我们同样可以正常访问网页，但这个过程中Web服务器识别出的真实IP就不再是我们本机的IP了，
    就成功实现了IP伪装，这就是代理的基本原理。
'''

'''
1、通过requests来进行代理设置
'''
import requests
from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.kuaidaili.com/free'
header = {
    'Accept-Encodin': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

}
response = requests.get(url, headers=header)
'''
爬虫小窍门，
1、通过find_all找到所有标签为tr的网页，在此基础上，再用find_all找到该结构下所有的td标签；
2、方便把ip地址和端口取出来，比用xpath简单；
'''
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('tr')
proxy_list = []
for i in items[1:]:
    tds = i.find_all('td')
    ip = tds[0]
    port = tds[1]
    proxy = {'http': 'http://' + ip.text + ':' + port.text}
    proxy_list.append(proxy)
for i in range(len(proxy_list)):
    print(proxy_list[i]['http'])
    try:
        response = requests.get('http://219.141.235.67:28088/login', proxies=proxy_list[i])
        print(response.url)
    except requests.exceptions.ConnectionError as e:
        print('错误:', e.args)
    sleep(3)
'''
2、通过urllib.request代理设置
'''
# import urllib.request
#
# for i in range(len(proxy_list)):
#     print(proxy_list[i])
#     #创建处理器
#     proxy_head=urllib.request.ProxyHandler(proxy_list[i])
#     #创建opener
#     opener=urllib.request.build_opener(proxy_head)
#     try:
#         print(opener.open('http://httpbin.org/ip',timeout=3).read())
#     except Exception as e:
#         print(e.args)

'''
3、selenium代理设置
'''
import requests
from bs4 import BeautifulSoup
import telnetlib

url = 'https://www.kuaidaili.com/free'
header = {
    'Accept-Encodin': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('tr')
proxy_list = []
for i in items[1:]:
    tds = i.find_all('td')
    ip = tds[0]
    port = tds[1]
    proxy = {'http': ip.text + ':' + port.text}
    proxy_list.append(proxy)
# print(proxy_list)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

opt = webdriver.ChromeOptions()
# 设置代理
p = '222.74.73.202:42055'
for i in range(len(proxy_list)):
    print(proxy_list[i]['http'])
    opt.add_argument("–proxy-server=http://" + proxy_list[i]['http'])
    driver = webdriver.Chrome(chrome_options=opt)
    driver.delete_all_cookies()
    driver.get('https://www.baidu.com')
    sleep(3)
    print(driver.current_url)

    # #通过telnetlib方法查看ip代理是否有效
    try:
        telnetlib.Telnet(proxy_list[i]['http'].split(':')[0], proxy_list[i]['http'].split(':')[1], timeout=5)
        print('代理ip成功')
    except:
        print('代理ip无效')
    driver.quit()
