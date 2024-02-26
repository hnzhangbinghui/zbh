# -*- coding= utf-8 -*-
# @Time: 2024-02-26 15:46
# @Author： Zbh

from zbh.Interface_automation import api_run

r=[('login', '测试通过'), ('post查询', '测试失败'), ('get查询', '测试通过')]
import csv

result_path=r"C:\Users\zhangbinghui\PycharmProjects\zbh\Interface_automation\test_result.csv"




def write_csv(filename,results):
    '''
    :param filename: string 需要写入的文件名称
    :param results:  [{data1},{data2},...] 写入的内容
    :return: 无
    '''
    # with open(filename,'w+') as cf:
    #     headers="describe,test_result".split(",")
    #     writer=csv.DictWriter(cf,fieldnames=headers,lineterminator="\n")
    #     writer.writeheader()
    #     # writer.writerow(res)
    #     if results.__len__() > 0:
    #         for res in results:
    #             writer.writerow(res)
    #     cf.close()
    with open(filename,'w+',newline='') as cf:
        writer=csv.writer(cf)
        if results.__len__() > 0:
            for res in results:
                writer.writerow(list(res))
        cf.close()






write_csv(result_path,api_run.test_api())














