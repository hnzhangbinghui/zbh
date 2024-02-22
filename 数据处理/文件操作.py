'''
os.walk()方法；
1、主要用来遍历一个目录内哥哥子目录和子文件；
2、是一个简单易用的文件，目录遍历器，可以高效处理文件，目录方便的问题；
os.walk(top[,topdown=True[,onerror=None[,followlinks=False]]])
解释：top，是遍历目录的地址，返回的是一个三元组（dirpath，dirnames，filenames）；
    topdown，可选，为True则优先遍历top文件夹，与top文件夹中每一个子目录；否则优先遍历top的子目录（默认是开启）；
    onerror，可选，需要一个callable对象，当walk需要异常时，会调用；
    followlinks，可选，如果是True，则会遍历目录下的快捷方式（linux的软连接）实际所指的目录（默认关闭）；如果是False，则
    优先遍历top的子目录；
三元组：
dirpath，是string，代表目录的路径；
dirnames，是list，包含了dirpath下所有子目录的名字；
filenames，是list，包含非目录文件的名字；
'''
import os
def walkOperation():
    path=r"C:\Users\zhangbinghui\PycharmProjects\anaconda\数据处理"
    for dirpath,dirnames,filenames in os.walk(path):
        print('路径是：',dirpath)
        print('目录下的文件',dirnames)
        print('非目录文件名称',filenames)
    for w in os.walk(path):
        print('直接返回三元组：',w)
        print('该目录下的所有文件：',w[2])

# walkOperation()

'''
1、读写文件是最常见的IO操作，python内置了读写文件的函数，用法和C是兼容的；
2、在磁盘上读写文件是有操作系统提供的，现代的操作系统是不允许普通的程序直接操作磁盘；
3、读写文件就是请求操作系统打开一个文件系统（通常称为文件描述符），通过操作系统提供的接口
    从这个文件对象中读/写文件；
4、open()函数，f=open('file_path',mode='r'),如果文件不存在，则会抛出IOError的错误；
    并且给出错误码和详细的信息，告诉你文件不存在；
5、mode的各种模式：r只读；r+读写（这两个若文件不存在就会报错）；w只写；w+读写；a只写；a+读写（这两个是在尾部追加写）；
    wb只写二进制字符串，写入bytes；rb只读二进制字符串，返回bytes（文件不存在会报错）；
6、如果文件打开，则通过read()方法可以一次读取文件的全部内容，python把内容读到内存，用一个str对象表示；
7、最后一步调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，
    并且操作系统同一时间能打开的文件数量也是有限的；
8、由于文件读写时有可能会产生IOErroe，一旦出错，后面的f.close()就不会调用，所以，为了保证无论是否出现都能正确关闭文件，
    我们可以使用try...finally来实现；
9、open()和with open()区别，open需要主动调用close(),with不需要；
10、open读取文件时发生异常，没有任何处理，with有很好的处理上下文的异常；
11、with可以同时操作多个文件；
with open("test/test.py", 'r') as f1, open("test/test2.py", 'r') as f2:
    print(f1.read())
    print(f2.read())
12、写文件，写文件和读文件是一样的，唯一区别是调用open()函数时，需要将mode参数改成可写的模式；
    可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件；
13、写文件的原理，当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存换出起来，空闲时再慢慢写入；
    只有调用close()方法时，操作系统才保证没有把写入的数据全部写入磁盘，而忘记调用close()的后果是数据坑你只写了
    一部分，剩下的丢失了；所以还是用with语句比较好；
14、关于字符编码，要写入特定编码的文本文件时，要跟open函数传入encoding参数，自动转换为指定编码，默认是None；
15、如果编码不规范的文件，会遇到UnicodeDecodeError文件，如果想要忽略这些报错，可以在open函数中加入字段errors=None解决；

'''
import os
def openOperation():
    file_path=r"C:\Users\zhangbinghui\PycharmProjects\anaconda\数据处理\test.txt"
    with open(file_path,'r') as f:
        a_data=f.readlines()
        print('读取所有数据：',type(a_data),a_data)
        print('读取某个字段：',a_data[0].strip())
    print("*"*50)
    with open(file_path,'a+') as f:
        f.write("\n通过with方法写入文件，不需要调用close方法；")
        f.write("\n!@#$%^&*()")
    #读文件
    try:
        f=open('test.txt','r')
        all_data=f.read()
        print('读取所有数据：',type(f.read()),'\n',all_data,len(all_data))
        print('读取某些数据：',all_data[:12])
    finally:
        if f:
            f.close()
    #写文件
    print("*" * 50)
    try:
        f = open('test.txt', 'a+')
        f.write("\n通过open函数写入内容")
        f.writelines("\n!@#$%^&@#$%！！")
    finally:
        if f:
            f.close()

openOperation()









