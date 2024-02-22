import unittest
import mock


# def add(self, a, b):
#    """两个数相加"""
#    pass
#
# class TestSub(unittest.TestCase):
#     def test_sub(self):
#        # 创建一个mock对象 return_value代表mock一个数据,相当于把return_value的值给了add；
#         mock_add = mock.Mock(return_value=13)
#         # 将mock对象赋予给被测函数
#         add = mock_add
#         # 调用被测函数,result的值就是return_value的值，而add返回的值没有意义；
#         result = add(5, 5)
#         # 断言实际结果和预期结果
#         self.assertEqual(result, 15)

class SubClass(object):
    def add(self, a, b):
        return a + b


class TestSub(unittest.TestCase):
    def test_sub(self):
        # 初始化被测试函数类实例
        sub = SubClass()
        # 创建一个mock对象，return_value代表mock的一个数据；
        # 传递side_effect关键字参数，会覆盖return_value参数值，使用真实的add方法参数
        '''
        side_effect，这里给的参数值是sub.add相当于add方法的地址，当调用add方法时就会调用真实的add方法；
        简单理解为，传递了side_effect参数且值为被测试函数地址时，mock不会其作用，两种不可共存；
        另外，side_effect接受的是一个可迭代序列，当传递多个值时，每次调用mock时会返回不同的值；
        '''

        sub.add = mock.Mock(return_value=15, side_effect=sub.add)
        # 调用被测试函数
        result = sub.add(5, 5)
        print('\n返回结果的值是：',result)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
