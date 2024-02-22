
#1、不带参数的构造方法
class Test():
    def __init__(self):
        print("自动调用构造方法")
        self.name="python"
# t 对象，隐式调用了手动创建的 __init__()构造方法；
t=Test()
print(t.name)
#2、带参数的构造方法
class Case():
    def __init__(self,name,age):
        print("自动调用构造方法")
        #初始化实例对象
        self.name=name
        self.age=age
        self.text="类属性，大家共享"
    def test(self):
        #定义一个test实例方法
        print(self.name,self.age)
        print('Myname is %s,年龄是 %s' %(self.name,self.age))
        print('共享1：',self.text)
    def test2(self,value):
        # 定义一个test实例方法
        self.name = value  # 如果实例对象重新赋值，则用该值；
        print(self.name, self.age)
        print('Myname is %s,年龄是 %s' % (self.name, self.age))
        print('共享2：', self.text)
c=Case('python','11')
c.test()
c.test2('zbh') #修改实例对象name的值；












