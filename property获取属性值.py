

class TestCase():
    def __init__(self,name):
        self.__name=name
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def delName(self):
        self.__name=None
    name=property(fget=getName,fset=setName,fdel=delName,doc='property测试')
t=TestCase
print(t.name.__doc__)

t=TestCase('实例对象t')
print(t.name)

t.setName('通过set设置')
print(t.name)

del t.name
#getName return的是私有属性__name，注意不是name，不然会先入死循环；
print(t.getName(),t.name)


















