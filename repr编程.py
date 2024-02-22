class A:
    def __repr__(self):
        return 'test'
aaa = A
print(aaa)
print(repr(aaa))
print(str(aaa))

class Test():
    def __init__(self):
        self.name='python'
        self.url='http://www.baidu.com'
    def __repr__(self):
        return f'{self.name+"  is  "+self.url}'
b=Test()
print(b)
print(str(b))
print(repr(b))












