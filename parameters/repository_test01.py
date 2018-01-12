#!/usr/bin/python2
#coding=utf-8

import csv

# enumerate可以把list变成索引序列
file_1 = open(r'C:\Users\Administrator\PycharmProjects\data\repository_test01.csv', 'r')
list_1 = csv.reader(file_1)
for row, pars in enumerate(list_1):
    # 从第二行开始取数据
    if row >= 1:
        # csv编码为gb2312，decode将gb2312转义为unicode,encode将unicode转为gb2312
        category = pars[0].decode('gb2312')
        title = pars[1].decode('gb2312')
        content = pars[2].decode('gb2312')
        file_name = pars[3].decode('gb2312')
        department = pars[4].decode('gb2312')
        post = pars[5].decode('gb2312')
        position = pars[6].decode('gb2312')
        label = pars[7].decode('gb2312')
        username = pars[8].decode('gb2312')
file_1.close()