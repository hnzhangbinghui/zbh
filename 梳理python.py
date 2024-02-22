# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 10:18:57 2022

@author: zhangbinghui
"""
'''
1、判断某个字符串是否包含指定的字符串
    1、find()，获取值时，如果要查找的值不存在，会返回-1；从字符串左边开始查询子字符串匹配到第一个索引（从0开始）；
    2、rfind(),从字符串右边开始查询字符串匹配到第一个索引（从0开始）；
    3、index()，获取值的索引时，如果不存在，会报错；从字符串左边开始查找子字符串匹配到第一个索引（从0开始）；
        str.index(sub, start=None, end=None),作用：查看sub是否在字符串中，在的话返回索引，且只返回第一次匹配到的索引；
        若找不到则报错；可以指定统计的范围，[start,end) 左闭区间右开区间
    4、rindex()，从字符串右侧开始查询字符串匹配到的第一个索引（从0开始）；
    5、count(),查找子字符串的次数；str.count( sub, start=None, end=None)，统计子字符串的数量，可以指定统计的范围，
        [start,end]，左闭右开区间；
    6、str.split(str="",num=string.count(str))，将字符串按照str分隔列表，如果参数num有指定值，则分隔num+1个字符串；
    7、str.strip(chars=""),移除字符串头尾指定的字符串序列chars，默认为空格；
    8、str.lstrip(chars="")，移除字符串头部指定的字符串序列chars，默认为空格；
    9、str.replace(old,new,count=-1)，把字符串中的old（旧字符串）替换成new（新字符串），count代表最多替换多少次，
        默认-1代表全部替换；
    10、str.join(sequence)，将序列中的元素以指定的字符链接生成一个新的字符串；举例：print('_'.join(list))；
        ''.join(lists)，是最常见的将列表，元祖转成字符串的写法；列表里面只能存放字符串元素，其他类型的元素会报错；
        元祖也能传进去；
    11、str.upper()，将字符串都变成大写字母；
    12、str.lower()，将字符串都变成小写字母；
    13、str.startswith(prefix,start=None,end=None)，检查字符串是否以指定的字符串开头，如果是则返回True，否则返回False，
        可以指定统计的范围，start，end是左闭右开的区间；
    14、str.endwith(self,suffix,start=None,end=None)，是结尾；
    15、str.isdigit()，检查字符串是否只有数字组成；是就返回True，否则返回false；
    16、str.isalpha()，检查字符串是否只有字母组成；
    17、str.splitlines([keepends])，将字符串按照行('\n','\r','\r\n')分隔；
    18、
    
    
'''
'''
1、loguru库，不仅能减少频繁的配置过程还能实现和logging类似的功能，还能保证日志记录的线程进程
    安全，又能够和logging相兼容，并进一步追踪异常也能进行代码回溯；
2、loguru库，可以直接通过导入它本身封装好的logger类就可以直接进行调用；
3、logger本身就是一个已经实例化好的对象，如果没有特殊的配置要求，那么自身的就已经带有通用的配置参数，
    同时它的用法和logging库输出日志时的用法一致；
4、loguru的日志输出还带上了不同颜色样式；
5、loguru保留日志文件，把日志保存到文件中，loguru通过add()方法，就可以配置一个日志文件；
6、Lloguru默认输出格式包含【时间，级别，模块名，行号及日志信息】,不需要手动创建logger，可直接使用；
7、logger.add(lpath,encoding='utf-8',enqueue=True,rotation='50MB',compression='zip',retention="10 days")
    lpath是日志的保存路径；encoding=“utf-8’，避免出现乱码；
    enqueue=True代表异步写入，大概是在多线程同时往日志文件写日志时使用队列达到异步功效；
    rotation可以理解成日志的创建时机，可以有多种写法；
        rotation=‘500MB’，当日志达到50M时就会重新生成一个文件；
        rotation=“12:00”，每天12点会创建新的文件
        rotation=‘1 week’，每隔一周创建一个log；
    retention，配置日志最长保留时间，官方例子：1 week，3 days，2 months；
    compression，配置文件的压缩格式，可以配置常见格式是zip，tar，gz，tar等；
8、loguru提供了字符串格式化输出日志功能，可以直接配置变量，也可以获取外部变量；
    logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')
    n1 = "cool"
    n2 = [1, 2, 3]
    logger.info(f'If you are using Python {n1}, prefer {n2} of course!')
9、

'''
from loguru import logger
from 数据处理.log import Loggings
import time
import os
def get_nowtime():
    return time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))

str="string test string test"
find1='str'
find2="test"
# path=r'C:\Users\zhangbinghui\PycharmProjects\anaconda\log'
# log_path=time.strftime("%Y-%m-%d_%H_%M_%S")+".log"
# lpath=os.path.join(path,log_path)
#
#
# logger.add(lpath,encoding='utf-8',enqueue=True,rotation='50MB',compression='zip',retention="10 days")
# a="logurur日志输出"
# logger.info('输出字符串长度：{},{name}',len(str),name="长度")
# logger.debug(f'输出字符串长度：{a}')
# logger.error('输出字符串长度：',len(str))
# logger.warning('输出字符串长度：',len(str))
# print('字符串长度：',len(str))
print('判断find1是否在str中：',find1 in str)
print('判断find1不在str中：',find1 not in str)

print('从str中查找find1：',str.find(find1))
print('从str中查找find2：',str.find(find2))

print('从str中右侧查找find1：',str.rfind(find1))
print('从str中右侧查找find2：',str.rfind(find2))

print('从str中通过index查找find1：',str.index(find1))
print('从str中通过index右侧查找find1：',str.rfind(find1))

print('从str中查找字符串出现的次数：：',str.count('t'))


name="python"
age=12
print(f"my name is {name},age is {age}")
print("my name is {},age is {}".format('java',12))

print("python".encode(encoding='utf-8'))
print(b'python')





