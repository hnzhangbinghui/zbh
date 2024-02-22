class PoloBlog():
    # 类属性
    name = 'aaaaaaaaaaa'
    def __init__(self,name):
        self.name=name

    # # 类方法, 添加装饰器
    # @classmethod
    # def class_func(cls):
    #     print("class_func cls 对象的 id ", id(cls))
    #     cls.sum += 1
    #     print("类属性 sum ", cls.sum)
    def test(self):
        print("类方法调用实例方法！！！")
        self.name='实例属性'
        print('访问的是实例属性：',self.name)
        print('访问类属性：',PoloBlog.name)


    # @classmethod
    # def class_func_twi(cls):
    #     print("class_func_twi cls 对象的 id ", id(cls))
    #     cls.sum += 1
    #     print("类属性 sum ", cls.sum)
    #     #类方法调用实例方法
    #     cls.test(cls)


# PoloBlog.class_func()
# PoloBlog.class_func_twi()
blog=PoloBlog("类属性")
blog.test()
