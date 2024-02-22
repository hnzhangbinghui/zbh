#继承
class Grandpa():
    def grandpa(self):
        print('爷爷级别的类')
class Parent(Grandpa):
    #构造方法
    def __init__(self,name):
        self.name=name
    def test1(self):
        print('打印父类',self.name)
class Child(Parent):
    def test1(self):
        super().test1()
        print('打印子类')
    def test2(self):
        print('第一个子类',self.name)
class Child2(Parent):
    def test3(self):
        print('第二个子类；',self.name)
# a=Parent('fuji')
# a.test1()
b=Child('child')
# b.test1()
b.test1()
# b.grandpa()
# c=Child2('child2')
# c.test1()
# #继承爷爷级别的方法；
# c.grandpa()






