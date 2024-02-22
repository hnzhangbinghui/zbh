from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return f(*args, **kwargs)
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func(*args, **kwargs):
    a = list(args)
    k = kwargs.keys()
    v = kwargs.values()
    print('原始值：',args,kwargs)
    return a, k, v


can_run = True
print(func(1, 2, 3, 4, a="python"))

can_run = False
print(func('a', 'b', 'c', 'd', 'e', a="name", b="python"), ',', func.__name__)

print("************在函数中嵌入装饰器*******************")
from functools import wraps


def logit(logfile=r'C:\Users\zhangbinghui\PycharmProjects\anaconda\zbh\out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + '  was called'
            print(log_string)
            # 打开logfile,并写入内容；
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit(logfile=r"C:\Users\zhangbinghui\PycharmProjects\anaconda\zbh\out2.log")
def myfunc1():
    pass


myfunc1()




