class Person():
    __sum = 1000

    # 构造方法
    def __init__(self, name):
        self.__name = name

    # 私有方法
    def __getName(self):
        print('name is :', self.__name)

    def getSiyou(self):
        print('获得私有变量的值：', Person._Person__sum, self.__sum)

'''
无论是类对象还是实例对象，都可以通过  ._类名__名称 ,来调用私有属性或者方法，这算是一种简介调用；'''
# 调用类的私有属性
print(Person._Person__sum)
# 生成实例对象，并给构造方法name赋值；
a = Person('python')
a.getSiyou()
a._Person__getName()
