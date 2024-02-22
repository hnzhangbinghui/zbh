class Test():
    sum=100
    def __init__(self,name):
        self.name=name
    def test(self):
        print('姓名是：',self.name)
    def testage(self):
        print('通过setattr添加',self.age,self.name)

t=Test('zbh')
print(t)
print('************hasattr********************')
print('实例对象--实例属性',hasattr(t,'name'))
print('实例对象-类属性',hasattr(t,'sum'))
print('类对象-类属性',hasattr(Test,'sum'))
print('类对象--实例属性',hasattr(Test,'name'))
print('************getattr********************')

print('得到实例对象-实例属性',getattr(t,'name'),t.name)
print('得到实例对象-类属性',getattr(t,'sum'),t.sum)
print('得到类对象-类属性',getattr(Test,'sum'),Test.sum)
print('类属性--实例对象（会报错，只有设置默认值）',getattr(Test,'name','默认值'))

print('************setattr********************')

setattr(t,'name','zhangbinghui')
setattr(t,'age',11)
print('设置后获取最新的name值：',getattr(t,'name'),getattr(t,'sum'))
'''
__dict__ 是类的内置属性，用于以字典的形式存储类里的属性（实例属性），也就是存储self.xxx 的属性；
'''
print(t.__dict__)

#设置一个新的实例方法
setattr(t,'pritnameage',lambda self:f"姓名：{self.name} 年龄：{self.age}")
print(t.__dict__)
print(getattr(t,'pritnameage'))
print(t.pritnameage(t))
t.testage()

print('************delattr********************')
print(t.__dict__)
delattr(t,'age')
delattr(t,'pritnameage')
print(t.__dict__)
'''
__name__ 是python的内置变量，它存储模块的名称；同时还可以反应一个包的结构；
python的模块既可以被调用，也可独立运行；而被调用时__name__存储的是py文件名（模块名称）
如果一个模块被独立运行时存储的是 __main__；
模块被执行时，__name__等于文件名（包含后缀.py）；
如果import到其他模块中，则__name__等于模块名称（不包含后缀）；
而‘__main__’等于当前执行文件的名称，包含后缀。所以当模块被执行时，__name__=='__main__'结果为真；
而当前模块被import到其他模块中，__name__=='__main__'结果为假，就不调用对应的方法；
'''
print(__name__)
import sys
print(sys.modules[__name__])







