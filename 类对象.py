class Person():
    pass
#打印类对象和内存地址
print(Person)
print(id(Person))
'''
1、类对象支持两种操作：属性引用和实例化；
2、属性引用，使用python所有属性引用的标准语法，obj.name;
3、有效的属性名称是类对象被创建时存在于类命名空间中的所有名称；
4、实例化就是调用类对象，从而创建一个实例对象；c=MyClass(),创建类的新实例并将对象分配给局部变量c；
5、实例对象，通过类实例化操作生成对象就是实例对象；
6、一个类可以有多个实例化，生成多个实例对象；
7、面向对象编程是：1）设计类，2）创建类实例对象；3）实例对象调用方法；
8、创建实例对象详解，1）在内存中为对象分配空间；2）初始化方法 __init__ 为对象初始化；3）对象创建后，内存中就有一个类的实例对象；
'''
class MyClass:
    """A simple example class文档字符串"""
    i = 12345
    def f(self):
        return 'hello world'
print('返回变量i的值：',MyClass.i)
print('返回函数对象：',MyClass.f)
print('返回当前类的文档字符串：',MyClass.__doc__)
class person():
    def __init__(self, name):
        self.name = name
        print(f"init-{self.name} ", id(self))

    def test(self):
        print(f"test-{self.name} ", id(self))

p1 = person("p1")
print("p1-", id(p1))
print("p1 fun-", id(p1.test))

p2 = person("p2")
print("p2-", id(p2))
print("p2 fun-", id(p2.test))









