import time
import datetime

print('1从1970-01-01至今的描述：', time.time())
# print('计算cpu的执行时间：',time.clock())

print('自定义时间格式转换：', time.strftime("%Y-%m-%d_%H:%M:%S"))
# 1、打印本地时间，time.localtime(second=None),把时间戳转换成相对于1970-01-01的本地时间，
# 不传seconds参数，默认打印当时的本地时间；
curr_time = time.localtime()
print('获得本地时间：', type(curr_time), curr_time)
print('获取当前时间对应的某个值：', curr_time.tm_year, curr_time.tm_hour)
# 2、把时间戳转换成固定格式字符串时间，ctime(seconds=None)，不传seconds参数时，默认转化当前时间；
print('转化当前时间：', time.ctime())

# 3、把元祖形式的结构化时间转换成时间戳；
# mktime(p_tuple)，把元祖形式的结构化时间转化成时间戳；

print('转换为时间戳：', time.mktime(time.localtime()))

# 4、datetime模块，打印格式化时间
# datetime.datetime.now(),打印格式化时间，这种格式大多用于日志打印中；
print('打印格式化时间', datetime.datetime.now())
