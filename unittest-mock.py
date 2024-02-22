import unittest
from unittest import mock
# def test():
#     print('test')
#
#
# result = mock.Mock(return_value='zbh', side_effect=test())
# # print(result,type(result))
# print(result.return_value)
# # print(result.side_effect)
class Test01(unittest.TestCase):
    def weather(self):
        '''天气接口'''
        # result={'result':'雪','status':'下雪了'}
        pass
    def weather_result(self):
        '''模拟天气接口返回值'''
        result = Test01.weather(self)
        if result['result'] == '雪':
            print('下雪了')
        elif result['result'] == '雨':
            print('下雨了')
        elif result['result'] == '晴天':
            print('晴天！！')
        else:
            print('返回值错误')
        return result['status']
    def testXiaxue(self):
        '''模拟下雪天场景'''
        mock_xue_result = {'result': "雪", 'status': '下雪了'}
        Test01.weather=mock.Mock(return_value=mock_xue_result)
        status=Test01.weather_result(self)
        self.assertEqual(status,'下雪了')
        self.assertIn(status,'下雪了')
    def testXiayu(self):
        mock_yu_result={'result': "雨", 'status': '下雨了'}
        Test01.weather=mock.Mock(return_value=mock_yu_result)
        status=Test01.weather_result(self)
        self.assertEqual(status,'下雨了')
if __name__=='__main__':
    unittest.main(verbosity=2)









