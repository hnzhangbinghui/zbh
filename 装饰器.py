'''
1、python中的函数，一切结尾对象；
'''


def hi(name="python"):
    return "hi," + name


print('直接调用：', hi())

# 把一个函数赋值给一个变量，如果函数名不带小括号，就表示不是在调用hi函数，而是将他放在greet变量里头；
# 但是，获得变量要加括号表示调用函数，才能获得对应的值；如果直接带括号，表示调用函数；
# 小结：小括号放到后面，这个函数就会执行，如果不放小括号在后面，那么他就可以导出传递，并且赋值给别的变量而不去执行他；
greet = hi
print('不带括号的赋值：', greet())
greet2 = hi()
print('带括号的赋值：', greet2)

# 先删除函数，在调用函数，就会报错；
# del hi
# print(hi())
'''
2、在函数中定义函数；下面展示了无论何时你调用hi函数，greet和welcome将会同时被调用；
    但是，greet和welcome函数，在hi函数之外是不能访问的；
    函数中可以嵌套函数；同样，函数也能返回函数；
'''
print("************函数嵌套函数*************************")


def hi(name="python"):
    print("now you are inside the hi() function")

    def greet():
        return "在hi函数内定义greet函数。"

    def welcome():
        return "在hi函数内定义welcome函数。"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function.")


hi()
print("******************函数返回函数***************************")


def hi(name="python"):
    def greet():
        return "在hi函数内定义greet函数。"

    def welcome():
        return "在hi函数内定义welcome函数。"

    if name == 'python':
        return greet
    else:
        return welcome


a = hi()
print('执行返回函数：', a())
print('不执行返回函数：', a)
print("******************将函数作为参数传给另一个函数******************")


def hi():
    return "hi,python"


def hi2(func):
    print("把hi函数作为hi2函数的参数进行传递；")
    print(func)


hi2(hi())

print("******************”开始第一个装饰器“******************")


# 相当于一个装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell.")


a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
print(a_function_requiring_decoration)
print(a_function_requiring_decoration())

print("*******使用@的装饰器****************")


@a_new_decorator
def test():
    print("装饰器调用测试！！")


print(test())
print(test.__name__)
'''
通过test.__name__得到的是wrapTheFunction，这里的函数被wrapTheFunction替代了，它重写了我们的函数名称和
注释文档（docstring）。
python可以通过function.wraps，来解决这个问题；
@wraps接受一个函数来进行装饰，并加入了复制函数的名称，注释文档，参数列表等功能；
'''
# 优化装饰器代码
print("**********优化装饰器*************")
from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def testaa():
        print("装饰器开始运行 ......")
        print(121213 * 43143)
        a_func()
        print("装饰器运行结束。")
        a_func()
        print("多次调用！！")
        a_func()

    return testaa


@a_new_decorator
def test2():
    print("装饰器调用测试")


test2()
print(test2.__name__)

'''
添加多个装饰器；在函数的前后添加相应的响应的功能；
'''


def outer(func):
    def login():
        print("登录成功")
        func()

        def logout():
            print("退出成功！！")
        return logout()
    return login
def outer2(func):
    def test_data():
        print("数据链接成功...")
        func()
    return test_data
@outer
@outer2
def test1():
    print("测试1")
@outer
def test2():
    print("测试2")
@outer
def test3():
    print("测试3")
@outer
def test4():
    print("测试4")
test1()
test2()
test3()
test4()
