import random

# 1、random.random(),返回0-1之间的随机浮点数；
print('生成0-1之间的随机浮点数：', random.random())
print('生成0-1之间的随机浮点数,并保留两位小数：%.2f' % random.random())

# 2、random.uniform(a,b),返回限定范围的随机浮点数，a,b可以是浮点数，也可以是正数；
print('限定范围的随机浮点数：', random.uniform(1, 1.5))

# 3、random.randint(a,b),返回限定范围内的正数，包括a,b；
import random

print('限定范围内的正数：', random.randint(1, 100))

# 4、random.randrange(start,stop=None,step=1),按步长step返回范围内随机整数，随机数包括左区间的起始值，不包括右边；
print('指定范围和步长的随机整数：', random.randrange(1, 5, 1))

# 6、random.choice(seq)，从序列中随机选择一个元素；
print('随机选择一个元素：', random.choice("python"))

# 7、random.sample(seq,k)，从序列中选取指定个数的元素；
import random

print('选取指定个数的元素：', random.sample([1, 2, 3, 4, 5, 6, 7], 3))
print('选取指定个数的元素(得到的是列表)：', random.sample('python', 3))

# 8、random.shuffle(seq)，把一个序列元素顺序打乱，俗称“洗牌”；
a = [1, 3, 5, 8, 9, 2, 4]
print('重新洗牌列表：', random.shuffle(a))
print(a)

# 实例，生成一个包括数字和字母的5位验证码
# chr(),返回返回代表指定unicode的字符；
import random


def func():
    code = ''
    for i in range(5):
        # s=random.choice([random.randrange(10),chr(random.randrange(65,91))])
        s = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'])
        code += str(s)
    print(code)


func()
