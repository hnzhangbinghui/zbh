#参考url:https://www.cnblogs.com/ananmy/p/13602964.html
'''
1、装饰器语法格式：被装饰的函数/类名=装饰器名（被装饰的函数/类名）；
2、实例1的func4函数被砖石，就是说@func1等价于func4=func1(func4)，输出“装饰器外层函数”和func2变量；
    func4()=func1(func4)()==func2()====>func2()函数中的func()就是func4()，最后结束；
3、被装饰的函数有参数时，只要修改内层函数func()，有对应参数即可；
4、在实际项目中，参数可以是0个或者多个，那么就用到了可变长参数（动态参数），元祖形式的可变长参数*args，和字典形式的**kwargs；
5、

'''
#实例装饰器1--被装饰的函数，无参数；
def fun1(func):
    print("装饰器外层函数")
    def fun2():
        print("执行func()函数之前")
        func()
        print("执行func()函数之后")
    return fun2
def func3():
    print("这是功能函数")
print("***************调用方法1******************")
func3=fun1(func3)
func3()
print("***************调用方法2******************")
@fun1
def func4():
    print("这是功能函数4")
func4()

'''
1、被装饰的类，无参数；
2、类里面实例方法的调用，首先要初始化一个对象MyClass()对象，再去调用里面的方法，即MyClass.withdraw()
3、同理，语法格式是：MyClass=login(MyClass)=recharge，那么，要初始化对象MyClass()，则MyClass()=login(MyClass)()=recharge(),
    即最后是调用recharge()函数，就是要修改内层函数，就是返回值要是一个MyClass()对象，也就是return a(),a是login的形参，
    装饰后传入的就是MyClass；
4、
'''
print("***************被装饰的类，无参数******************")
#函数装饰器
def login(a):
    print("这是登录函数")
    def recharge():
        print("这是充值函数")
        return a()

    return recharge

@login
class MyClass():
    def withdraw(self):
        print("这是取现函数")
MyClass().withdraw()





