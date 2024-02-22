class A():
    def test(self):
        print('AAAAAA')


class B():
    def test(self):
        print("BBBBBB")
# 继承了三个类，B，A，还有默认继承的object；


class C(B, A):
    def test(self):
        print('CCCCCCCC')


print('通过类对象调用，不是实例对象；查看方法搜素顺序：\n', C.__mro__)
# 得到的结果是：(<class '__main__.C'>, <class '__main__.B'>, <class
# '__main__.A'>, <class 'object'>)
C().test()
'''
1、在搜索方法时，是按照 __mro__ 的输出结果是从左往右的顺序查找；
2、如果在当前类（class C）中找到方法，就直接执行，不在搜索；
3、如果没有找到，就查找下一个类中 B 是否有对应的方法，如果有，则不在搜索，如果没有继续搜索A类；
4、如果找到最后一个类（class object）都没有找到对应方法，就报错；
'''
