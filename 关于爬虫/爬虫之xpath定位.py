# 参考url：https://blog.csdn.net/ai_sxy/article/details/86029108
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = 'http://www.ihain.cn/forum.php'
head_url = 'http://www.ihain.cn/'
import random
import lxml


def func_find_test(url):
    os.makedirs('./book/', exist_ok=True)
    header = {
        'Accept-Encodin': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

    }
    html = requests.get(url, headers=header).text
    # 实例化bs，传入参数待解析html内容和解析器；
    # html.parser是python内置的，方便兼容性好；lxml基于C，效率较高，需要额外安装包；
    # bs = BeautifulSoup(html, 'html.parser')
    bs = BeautifulSoup(html, 'lxml')
    # div=soup.xpath('/div')
    # 格式化输出(输出的内容更加格式化)
    # print(bs.prettify())
    # print('获得head标签的内容：\n',bs.head.prettify())
    # print('获得head标签下级的内容1：\n',bs.head.contents[1])
    meta_all = bs.head.find_all('meta')
    # print('获得head标签下级的内容2：\n', meta_all)
    # for m in range(len(meta_all)):
    #     print('通过.name得到标签名称：',meta_all[m].name)
    for d in bs.find_all('div'):
        print('得到标签属性：', d.attrs)
    print('*' * 30)
    a_all = bs.find_all('dt')
    for a in a_all:
        print('通过string得到标签内容：', a.string)
        print('通过text得到标签内容：', a.text)
    print('*' * 30)
    dt_all = bs.find_all('dt')
    for dt in dt_all:
        print('返回列表，标签下所有字标签：', dt.contents)
        print('得到dt标签的子节点，得到的是迭代器：', dt.children)
        for v in dt.children:
            print('子节点的具体的值：', v.name, v.text, v.get('href'))

    print('*' * 30)
    # 根据css语法搜索,直接搜索标签名，比find_all搜索的更全面
    a_css = bs.select('a')
    print('通过css进行搜索得到所有a标签：\n', a_css)
    for a in a_css:
        print(a.text, a.get('href'))
    print('*' * 60)
    # 通过css搜索class的值,在class前面添加 . 进行搜素；
    c_css = bs.select('.fl_icn_g')
    print('通过css搜索class的值：\n', c_css)
    # 通过css搜索id的值，在id的值前面添加 # ；
    print('#' * 60)
    d_css = bs.select('#category_3')
    print(d_css)


# func_find_test(url)


print('*' * 30 + '通过xpath进行定位' + '*' * 30)
url = 'http://www.ihain.cn/forum.php'
from lxml import etree

def fund_xpath_test(url):
    header = {
        'Accept-Encodin': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 '

    }
    rep = requests.get(url, headers=header)
    rep.encoding = 'gbk'
    # print(rep.text)
    # 把html字符串转换etree对象
    # h=etree.fromstring(html) #默认xml，语法严格，用来解析html标签不规范会报解析错误；
    # h=etree.HTML(html2) #html解析器，强度标签问题会自动补全；
    html = etree.HTML(rep.text)
    print('搜索a标签，得到元素对象：\n', html.xpath('//a'))  # 查询所有符合的返回列表，每一项是元素对象；
    # 提取标签属性值 格式：//查找标签/@属性名
    print('得到所有的href的值：\n', html.xpath('//a/@href'))
    # 获得标签内容，格式： //查找标签/text()
    print('得到所有的text的值：\n', html.xpath('//a/text()'))
    # 查找根据属性限制标签 ，格式://待查标签[@属性名=属性值]
    print('得到特定的标签值：', html.xpath('//img[@id="category_3_img"]/@title'))
    # 查询下一级，得到a的的标签内容能，以及链接；
    print('查询下一级节点，省略可以省略层级：', html.xpath('//dt/a/text()'), '\n', html.xpath('//dt/a/@href'))

    # etress对象和字符串互转
    str = etree.tostring(html)
    print('把etress对象转换为字符串：\n', str)


fund_xpath_test(url)

'''
# (了解)包含条件
# contains(@class, "class值")  适合没有id、name属性class属性
print(html.xpath('//div[@class="one"]/p[contains(@class, "first")]/text()')[0])
'''
#关于xml和xpath：
#1、用正则处理html文档很麻烦，可以先将html文件转换成xml文档，然后在用xpath查找html节点或元素；
#2、xml值得是可扩展标记语言，很类似html，设计宗旨是传输数据，xml标签需要我们自己定义；
#3、

'''
关于lxml库：
1、安装：pip install lxml;
2、lxml是一个html/xml的解析器，主要功能是如何解析和提取html/xml数据；
3、lxml和正则一样，是C来实现的，是一款高性能的python html/xml解析器，可以利用xpath语法，来快速定位特定元素及节点信息；
4、利用etree.HTML,，将字符串解析为html文档,xml格式；html=etree.HTML(text)
5、将字符串序列化html文档,reslut=etree.tostring(html);
6、
'''



'''
有关xpaht定位解析：
1、XPath（xml path language）是一门在xml文档中朝招信息的语言，可用来在xml文档中对元素和属性进行遍历；
2、chrome插件XPATH HelPer；Firefox插件xpath checker；
3、xpath的语法：
    1、nodename ，选取此节点的所有子节点；举例：bookstore，选择bookstore元素的所有子节点；
    2、/ ，从根节点选取； 举例：/bookstore，选取根元素bookstore；
    3、//,从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置；
    4、.(一个点) ,选取当前节点；
    5、..(两个点),x选取当前节点的父节点；
    6、@，选取属性；
    7、bookstore/book，选取所有bookstore的子元素的所有book元素；
    8、//book，选取所有book子元素，而不管他们在文档中的位置；
    9、bookstore//book，选择属于bookstore元素的后代的所有book元素，而不管他们位于bookstore之下的什么位置；
    10、//@lang，选取名为lang的所有属性；
4、谓语，用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中；
    1、/bookstore/book[1],选择属于bookstore子元素的第一个book元素；
    2、/bookstore/book[last()],选取属于bookstore子元素的最后一个book元素；
    3、/bookstore/book[last()-1],选取属于bookstore子元素的倒数第二个book元素；
    4、/bookstore/book[position()<3],选取最前面的两个属于bookstore元素的子元素的book元素；
    5、//title[@lang],选取所有拥有名为lang的属性的title元素；
    6、//title[@lang='eng'],选取所有title元素，且这些元素拥有值为eng的lang属性；
    7、/bookstore/book[price>35.00],选取bookstore元素的所有book元素，且其中的price元素的值须大35；
    8、/bookstore/book[price>35.00]/title,选取元素中的book元素的所有title元素，且其中的price元素的值大于35；
5、选取位置节点，xpath通配符可以用来选取未知的xml元素；
    1、*，匹配任何元素节点；举例：/bookstore/*，选取bookstore元素的所有子元素；
    2、@*，匹配任何属性节点； 举例：//*,选取文档中的所有元素；
    3、node()，匹配任何类型的节点；举例：//title[@*],选取所有带有属性的title元素；
6、选取若干路径：
    1、//book/title | //book/price，选取book元素的所有title和price元素；
    2、//title | //price，选取文档中所有title和price元素；
    3、/bookstore/book/title | //price，选取bookstore元素的所有title元素，以及文档中所有的price元素；





'''






















