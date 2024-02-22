import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

'''
解析find_all(),该方法搜索当前的所有tag子节点，并判断是否符合过滤器的条件；
格式：find_all(name,attrs,recursive,text,**kwargs)
解释：1、name,标签名，使用html比较签名来索引；div = soup.find_all('div')
    2、atters,可根据标签名，属性，内容查找内容，也可以使用双属性来查找元素；content = html.find(attrs = {'class':'p_opt','id':'card_1550_menu_content'})
    3、注意find_all()，返回的是一个列表，访问列表内容，访问列表内容使用下标；content[n],下标从0开始的；
    4、访问列表元素的下一级元素则使用  .contents[m] 来访问（也是从0开始）；
    5、嵌套查询：ul = html.find_all('ul')    #查找ul标签下的内容、嵌套选择
                for li in ul:
                    print(li.find_all('li')) #打印多个ul中的每一个
    6、
find(name,attrs,recursive,text,wargs)
解释：1、find用法和findall一模一样，但是返回的而是找到的第一个符合条件的内容输出
    2、注意find()，返回的不是列表，而是一个单个元素对象；
    3、想要访问该对象的子元素就直接使用 .contents[n]即可，不需要在添加下表；
'''
url = 'http://www.ihain.cn/forum.php'
head_url = 'http://www.ihain.cn/'
import random

def download_book(url):
    os.makedirs('./book/', exist_ok=True)
    header = {
        'Accept-Encodin': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

    }
    html = requests.get(url, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')
    id_list = ['category_3', 'category_135', 'category_26']
    for i in range(len(id_list)):
        div = soup.find_all('div', id=id_list[i])
        # print(div)
        list = []
        for a in div:
            b = a.find_all('td', class_='fl_g')
            for c in b:
                d = c.find_all('a')
                # 把对应的主页的标题和网站保存到txt文档中；
                with open('text.txt', 'a') as f:
                    f.write(d[1].text)
                    f.write(',')
                    f.write(os.path.join(head_url, d[1]['href']))
                    f.write(',')
                    f.write(str(requests.get(os.path.join(head_url, d[1]['href'])).status_code))
                    f.write('\n')
                # 得到网站网址，打开，并找到网页对应的帖子名称；
                d_url = os.path.join(head_url, d[1]['href'])
                # print(d_url)
                d_html = requests.get(d_url, headers=header).text
                d_soup = BeautifulSoup(d_html, 'html.parser')
                d_div = d_soup.find_all('table', id="threadlisttableid")
                a_list = []
                # 找到帖子所在的位置；
                for a in d_div:
                    a_text = a.find_all('a', class_='s xst')
                    a_list.append(a_text)
                # print(a_list[0])
                # 打印帖子所在模块标题
                print('*' * 20 + d[1].text + '*' * 20)
                with open('text.txt', 'a') as f:
                    f.write('*' * 20 + d[1].text + '*' * 20)
                    f.write('\n')
                # 得到具体帖子所在网址和帖子标题
                if len(a_list) != 0:
                    for i in range(len(a_list[0])):
                        with open('text.txt', 'a') as f:
                            f.write(a_list[0][i].text)
                            f.write(',')
                            f.write(str(os.path.join(head_url, a_list[0][i]['href'])))
                            f.write('\n')
                        # print(a_list[0][i].text,os.path.join(head_url,a_list[0][i]['href']))
                        # print(a_text[0].text,a_text[0]['href'])
                else:
                    with open('text.txt', 'a') as f:
                        f.write('没有内容，请查看具体网址！！\n')
                    # print('没有内容，请查看具体网址！！')

download_book(url)
