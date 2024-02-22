# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:55:02 2022
@author: zhangbinghui
"""
import unittest
from ddt import ddt, data, unpack, file_data
# 需要导入ddt包，然后TestCase类上采用@ddt进行装饰，测试方法上装饰@data(),data可以是数值，也可以是字符串；
from selenium import webdriver
from time import sleep


@ddt()
class TestCase(unittest.TestCase):
    '''
    #ddt直接放入数值；
    运行结果可以看到，只有一个测试方法，但是却运行了5（参数个数）个测试用例。
    这里的测试方法后，会被ddt加一个后缀，ddt会尝试把测试数据转化为后缀附在测试方法后，组成一个新的名字；
    '''

    @data(3, 4, 21, 23, "python")
    def test01(self, value):
        print('\n获得数据的值是：', value)

    '''
    使用复杂的数据结构时，需要用到@unpack，同时测试方法的参数需要使用你对应的多个；
    数据可以是元祖，列表，字典（字典的键必须对应上）；
    '''

    @data((2, 2), (3, 3), (6, 6), [8, 8], [9, 9], {'a': 111, 'b': 111})
    @unpack
    def test_02(self, a, b):
        print(a, b)
        self.assertEqual(a, b)

    # 从文件中读取文件
    @file_data(r'C:\Users\zhangbinghui\PycharmProjects\anaconda\zbh\aa.json')
    def test_03(self, j):
        print(j)
        self.assertIn(j, "zhangbinghui", msg="failed")

    @file_data(r"C:\Users\zhangbinghui\PycharmProjects\anaconda\zbh\bb.yaml")
    def test_04(self, y):
        # 得到的类型是列表；
        print(y)
        # for i in range(len(y)):
        #     print(y[i])


if __name__ == "__main__":
    unittest.main(verbosity=2)
