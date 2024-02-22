import csv

import json

import requests

import time

import unittest


def readCSV(self, filename):
    '''
    :param filename: ��Ҫ��ȡ�������ļ�
    :return: [{data1},{data2}...]
    '''

    datas = []

    try:

    # ��DictReader�ķ�ʽ��ȡ�����ļ���������json����ת��

    with open(filename, 'r') as csvfile:

    # ���ļ����ȡ��������ת�����ֵ��б�ĸ�ʽ

    reader = csv.DictReader(csvfile)

    for row in reader:

    data = {}

    data['id'] = row['id']

    data['url'] = row['url']

    data['token'] = str(row['token'])

    data['mobile'] = row['mobile']

    data['email'] = row['email']

    data['expect'] = json.dumps(row['expect'])
        if isinstance(row['expect'], dict) \
 \
        else row['expect']  # ���expect��ȡ�����Ĳ���json��ȡ��ԭֵ������תΪjson��ʽ���浽result��

    datas.append(data)

    return datas

    # ����ļ��Ҳ��������ؿյ�datas

    except FileNotFoundError:

    print("�ļ�������", filename)

    return datas


