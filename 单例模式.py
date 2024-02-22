class PoloBlog():
    def __new__(cls, *args, **kwargs):
        #1、自动调用 __new__
        print('分配内存地址！！')
        #2、为对象分配控件得到的引用复制给instance
        instance=super().__new__(cls)
        print(id(instance))
        #返回对象引用给python解释器
        return instance
    def __init__(self,name):
        self.name=name
    def test(self):
        print(f'获得init的值是：{self.name}')
p=PoloBlog('python')
print(id(p))
p.test()
'''
从运行结果可以看到两个内存地址是同一个，表名 __new__ 分配的对象引用的确传递给了 __init__ 方法的self参数；
'''
print('&'*20)
p2=PoloBlog('zbh')
print(id(p2))
'''
可以看到，两个对象p，p2都要各自的内存地址，则单纯的重写 __new__ 方法并不能实例单例模式；
'''
print('************单例模式*************')
#__new__ 实现单例模式的逻辑；单例，在整个应用程序中只有唯一的实例对象；
#1、定义一个类属性，来保存单例对象的引用；
#2、重写 __new__ 方法；
#3、如果类属性 is none，则调用父类方法分配内存控件，并赋值给类属性；
#4、如果类属性已有对象引用，则直接返回；

class TestDanLi():
    instance=None
    def __new__(cls, *args, **kwargs):
        #判断类属性是否为None
        if cls.instance is None:
            #2、为空，调用父类方法，给对象分配内存控件，并赋值给类属性；
            cls.instance=super().__new__(cls)
        #如果不为空，则直接返回类属性保存的对象引用；
        return cls.instance
    def __init__(self,value):
        self.value=value
        print(f'得到的值是：{self.value}')

a1=TestDanLi('111111')
a2=TestDanLi('222222222')
a3=TestDanLi('33333333')
#可以看到三个实例对象都是同一个，这就是单例模式；
print(id(a1),id(a2),id(a3))

'''
每次使用类名()创建对象时，python的解释器都会自动调用两个方法；
__new__分配空间；
__init__ 对象初始化；
所说的单例模式，就是针对 __new__ 方法进行重写的，创建多个实例对象都会得到同一个实例对象；
但是，初始化方法还是被多次调用；
'''

'''
想让初始化动作只执行一次：
1、定义一个类属性标记是否执行初始化动作，初始值是False；
2、在__init__方法中，判断类属性，如果是False，则执行初始化动作，然后设置为True；
3、如果True则直接跳过不执行；
'''
print('******初始化动作执行一次************')
class TestChuShiHua():
    instance=None
    init_flag=None
    def __new__(cls, *args, **kwargs):
        #判断类属性是否为None
        if cls.instance is None:
            #2、为空，调用父类方法，给对象分配内存控件，并赋值给类属性；
            cls.instance=super().__new__(cls)
        #如果不为空，则直接返回类属性保存的对象引用；
        return cls.instance
    def __init__(self,name):
        #判断是否为True，因为是实例方法，所以调用类属性要通过类属性
        if TestChuShiHua.init_flag:
            #如果是True，直接跳过不执行后续初始化动作；
            return
        #如果False，则执行；
        print('初始化动作')
        self.name=name
        #修改init_flag
        TestChuShiHua.init_flag=True
    def test(self):
        print('得到的值是：', f'{self.name}')
        print(TestChuShiHua.init_flag)


b1=TestChuShiHua('1111111')
b2=TestChuShiHua('')
b3=TestChuShiHua('333333')

b1.test()
b2.test()
b3.test()




