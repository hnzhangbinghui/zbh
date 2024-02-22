str="zhangBINGhui"
sub="h"
str2="我是测试"
def zhishidian():
    print("1、首字母大写：",str.capitalize())
    print("2、将大写转换为小写(只能转换英文字母)：",str.casefold())
    print("3、同2，将大写全部转换为小写：",str.lower())
    print("4、将小写全部转换为大写：",str.upper())
    print('5、统计子串的数量：',str.count(sub,3)) #可以设置查找的起始位置；
    print("6、返回str经过enconding编码后的字节：",str2.encode(encoding='UTF-8',errors="strict"))
    print("7、查找子串第一次出现的位置：",str.find(sub)) #可以设置查找的其实位置；
    print("8、字符串链接：",str.join(sub))
    a="我是测试"
    #str转换为gb2312编码
    print('str转换为gb2312编码',a.encode("gb2312"))
    print('str转换为utf-8编码：',a.encode("utf-8"))
    a_gb=a.encode('gb2312')
    print('先解码在编码：',a_gb.decode('gb2312').encode("utf-8"))
    print('编码后进行解码：',a_gb.decode('gb2312'))
    import chardet
    print(chardet.detect(a_gb))
zhishidian()






