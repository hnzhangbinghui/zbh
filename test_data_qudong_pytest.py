# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:55:02 2022
@author: zhangbinghui
"""
import pytest

from selenium import webdriver
from time import sleep

data = [("zhangbinghui", "123456"), ("zhangbinghui", "123456"), ("zhangbinghui", "123456")]


class TestCase():
    @pytest.mark.parametrize("a,p", data)
    # #有几组参数值，就执行几次，循环执行用例；
    def test_login1(self, a, p):
        print(a, p)
        driver = webdriver.Firefox()
        driver.get("http://219.141.235.67:18603/login")
        driver.implicitly_wait(10)
        account = driver.find_element_by_xpath("//input[@placeholder='登录账号']")
        account.click()
        account.clear()
        account.send_keys(a)
        passwd = driver.find_element_by_xpath("//input[@placeholder='密码']")
        passwd.click()
        passwd.clear()
        passwd.send_keys(p)
        sleep(2)
        driver.find_element_by_xpath(
            "//button[@class='el-button login-button el-button--default el-button--small']").click()
        sleep(5)
        assert "张冰辉" in driver.page_source
        sleep(2)
        driver.quit()

    '''
    重点，当装饰器@pytest.mark.parametrize装饰测试类时，会将数据集合传递给类的所有测试用例方法；
    “笛卡尔积”，多个参数化装饰器.
    如下：data1和data2会进行笛卡尔积，执行2*2次用例；
    '''
    data1 = ['zhangbinghui', 'zbh']
    data2 = ['123456', '123456']

    @pytest.mark.parametrize("a", data1)
    @pytest.mark.parametrize("p", data2)
    def test_login2(self, a, p):
        print(a, p)
        driver = webdriver.Firefox()
        driver.get("http://219.141.235.67:18603/login")
        driver.implicitly_wait(10)
        account = driver.find_element_by_xpath("//input[@placeholder='登录账号']")
        account.click()
        account.clear()
        account.send_keys(a)
        passwd = driver.find_element_by_xpath("//input[@placeholder='密码']")
        passwd.click()
        passwd.clear()
        passwd.send_keys(p)
        sleep(2)
        driver.find_element_by_xpath(
            "//button[@class='el-button login-button el-button--default el-button--small']").click()
        sleep(5)
        assert "张冰辉" in driver.page_source
        sleep(2)
        driver.quit()

    # 参数化传入字典,元祖要是只有一个值时，要带个逗号；
    data_dict = ({"account": "zhangbinghui", "passwd": 123456},)

    @pytest.mark.parametrize("d", data_dict)
    def test_login3(self, d):
        driver = webdriver.Firefox()
        driver.get("http://219.141.235.67:18603/login")
        driver.implicitly_wait(10)
        account = driver.find_element_by_xpath("//input[@placeholder='登录账号']")
        account.click()
        account.clear()
        account.send_keys(d["account"])
        passwd = driver.find_element_by_xpath("//input[@placeholder='密码']")
        passwd.click()
        passwd.clear()
        passwd.send_keys(d["passwd"])
        sleep(2)
        driver.find_element_by_xpath(
            "//button[@class='el-button login-button el-button--default el-button--small']").click()
        sleep(5)
        assert "张冰辉" in driver.page_source
        sleep(2)
        driver.quit()

    # 标记参数化
    @pytest.mark.parametrize("test_input,expected",
                             [("3+5", 8), ("2+4", 6), pytest.param("6*7", 42, marks=pytest.mark.xfail),
                              pytest.param("6*6",22,marks=pytest.mark.skip)])
    def test_login4(self, test_input, expected):
        assert eval(test_input) == expected


if __name__ == "__main__":
    pytest.main(["-vs"])
