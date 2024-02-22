
'''仅限位置参数是python3.8才有的新特性；新增了一个函数形参语法  /  ，添加了它，表示函数形参只能通过位置参数传递，
而不能通过关键字参数形式传递；'''
def test1(a,b,c):
    print(a,b,c)

'''
test2得到一些作为关键字参数传递的仅位置参数a，
在  /  形参前面的参数，只能通过位置参数传递；
'''
def test2(a,/,b,c):
    print(a,b,c)
#仅限关键字参数
def test3(a,*,b,c):
    print(a,b,c)

def test4(a,/,b,*,c):
    print('混合使用：',a,b,c)
if __name__=='__main__':
    test1(*[1,2,3])
    test2(*[1],b=2,c=3)
    test2(1,2,3)
    test3(a=1,b=2,c=3)
    test4(1,2,c=3)





















