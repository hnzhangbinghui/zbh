v = '123'
print(v)


print(eval(v))

x = 10
g = {'x': 5}
print('得到结果是8：', eval('x+3', g))

# print('没有的变量会报错：',eval('x+y+1',g))

a = 1
g = {'a': 2, 'b': 3}
l = {'a': 3, 'c': 4}
print(eval('a,b,c,a+b+c', g, l))
# 得到结果是：(3, 3, 4, 10)

json = "{'a':2,'b':3}"
print(type(json))
print(eval(json), type(eval(json)))
# 得到结果：{'a': 2, 'b': 3} <class 'dict'>
