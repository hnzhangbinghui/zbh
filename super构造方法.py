class Animal():
    def __init__(self,name):
        self.name=name
    def test1(self):
        print('Animal name is :',self.name)
#单独Animal调用方法；
Animal('AAAAAA').test1()
print('*'*30)
#Dog继承Animal，并重写父类方法；
class Dog(Animal):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def test1(self):
        print(self.name,self.age)
Dog('aaa',10).test1()
print('*'*30)
class Cat(Animal):
    def __init__(self,name,age):
        #调用父类的 init构造方法
        super(Cat, self).__init__(name)
        self.age=age
    def test1(self):
        #调用父类方法
        super(Cat,self).test1()
        print('Cat name/age is:',self.name,self.age)
Cat('小猫',11).test1()
