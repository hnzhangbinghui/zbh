'''
locals函数以字典的形式返回当前所在作用域的全部变量，
如果你在一个模块里执行locals函数，那么它返回的与globals函数返回值相同，
如果你在一个函数中执行locals函数，就只能返回这个函数所形成的局部作用域里的变量。

'''
def test(a, b):
    c = a + b
    d = c + 3
    # print(locals())
    return locals()


x = test(1, 2)
print(x)
print(type(x))


def create_sql(table, id):
    sql = "select * from {table} where id={id}".format(table=table, id=id)
    return sql

print(create_sql("user",2))



def create_sql2(table, id):
    sql = "select * from {table} where id={id}".format(**locals())
    #使用两个*表示解包，解包后作为参数传入format方法，**locals()等价于table=table, id=id
    return sql

print(create_sql2("user2",22))

print("#"*50)
#解包,*直接完成了列表、元组和集合的解包。
li = list(range(7))
tu = tuple(range(7))
se = set(range(7))

print(*li,*tu,*se)
#但是不能用**对字典解包，print(**{"name":"sian","name":25})会报错SyntaxError: invalid syntax。
#虽然不能用于直接输出，但是可以切片。
m={'a': 1, 'b': 2, 'c': 3, 'd': 6}
n={**m}
print(m)
print(n)

#生成器的解包

print(i for i in range(10))  #输出告诉你这是一个生成器对象。可以用生成器对象创建列表和集合，但是直接无法创建元组。
li = [i for i in range(7)]
se = {i for i in range(7)}
print(li,se)

#用*解包生成器对象
print(*[i for i in range(9)])






























