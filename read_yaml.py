import yaml
yaml_path = r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Data\testYaml.yaml"

'''
针对不同的需要，加载器有几种类型：
1、BaseLoader，仅加载最基本的yaml；
2、SafeLoader，安全加载yaml语言的子集，建议用于加载不受信任的输入（safe_load）；
3、FullLoader，加载完整的yaml语言，避免任意代码执行，用yaml.load(input)，发出警告时，
    就用fullloader；
4、UnsafeLoader，也称为Loader向后兼容性，原始的Loader代码，可以通过不受新人的数据输入轻松利用；

'''


def readYaml():
    with open(yaml_path, encoding='utf-8') as f:
        result = f.read()
        print('得到的是字符串的形式：', type(result), '\n', result)
        re = yaml.load(result, Loader=yaml.FullLoader)
        print('得到的类型是字典的形式：', type(re), re)
        print(re['login'][0]['account'])


readYaml()


'''
存储数据到yaml的方法
'''
write_path = r"C:\Users\zhangbinghui\PycharmProjects\anaconda\Data\write_Yaml.yaml"
write_data = {'unsorted_list': [10, 15, 12], 'sorted_list': [15, 12, 50],
              'url': 'http://www.baidu.com',
              'login': [{'account': 'zhangbinghui'}, {'passwd': 123456}]}


def writeYaml():
    with open(write_path, 'w', encoding='utf-8') as f:
        yaml.dump(write_data, f, Dumper=yaml.SafeDumper)
        f.close()


writeYaml()
