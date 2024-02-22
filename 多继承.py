#多继承
class Parent1():
    #构造方法
    def __init__(self,name):
        self.name=name
    def test1(self):
        print('父类1',self.name)
    def test11(self):
        print('父类1特有',self.name)
class Parent2():
    #构造方法
    def __init__(self,name):
        self.name=name
    def test1(self):
        print('父类2',self.name)
    def test22(self):
        print('父类2特有',self.name)
class Child(Parent2,Parent1):
    def test1(self):
        super().test1()
        print('打印子类')
    def test2(self):
        print('第一个子类',self.name)

a=Child('aaaa')
a.test1() #优先继承靠前的父类的方法；
#同时拥有所有父类的方法和属性；
a.test11()
a.test22()

print((dir(Parent1)))
