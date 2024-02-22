'''
1、pathlib,面向对象的文件系统路径；是一个从3版本开始能完全替代os。path的内置库；
2、pathlib和os.path的比较，
    当需要多个层级目录路径时，通过os.path需要嵌套写法，比如：project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
    而pathlib可以提供链式写法，简单明了；
    os.path只用于处理路径，如果你想在获取到路径下做一些事情，比如创建一个目录，就需要使用os模块；
    而pathlib可以额一站式搞定；


'''


from 数据处理.log import Loggings
import os
import pathlib
''' 获取当前目录以及上层目录的比较'''
v2=os.getcwd()
print('通过os获取路径：',v2)
#os通过嵌套式调用，就是层层嵌套来获取上上层目录；
print('os获得当前文件夹的上上层目录：',os.path.dirname(os.path.dirname(os.getcwd())))
v3=pathlib.Path.cwd()
print('通过pathlib获取路径：',v3)
#pathlib通过链式调用来获取；
print('获得当前文件夹的上上层目录：',pathlib.Path.cwd().parent.parent)

'''拼接目录,在当前目录的父级目录拼接test文件夹下的test.txt'''
print('os拼接目录：',os.path.join(os.path.dirname(os.getcwd()),'os_test','test.txt'))
print('pathlib拼接：',pathlib.Path.cwd().parent.joinpath('test','test.txt'))

'''创建文件夹并重命名'''
#在当前目录常见os_test文件夹；
# os.mkdir(os.path.join(os.getcwd(),'os_test'))
# #将os_path目录修改名称为os_test_rename;
# os.rename('os_test',os.path.join(os.getcwd(),'os_test_rename'))
# os.remove(os.path.join(os.getcwd(),'os_test_rename'))

#在当前目录下创建pathlib_test文件夹；
# pathlib.Path('pathlib_test').mkdir(parents=True,exist_ok=True)

# pathlib.Path('pathlib_test').rename('rename_pathlib')

'''pathlib常用基本方法'''

print('当前路径',pathlib.Path.cwd())
print('分隔路径(元祖)：',pathlib.Path.cwd().parts)
print('获得当前路径的根目录：',pathlib.Path.cwd().root)

curr_path=pathlib.Path.cwd()
print('判断当前是否是目录:',curr_path.is_dir())
print('判断当前是否是文件:',curr_path.is_file())
print('判断当前是否存在:',curr_path.is_file())
print('获得绝对路径：:',curr_path.resolve())
print('拼接字符串：',curr_path.joinpath('文件路径.py'))








