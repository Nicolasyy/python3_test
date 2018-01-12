#!/usr/bin/python2
#coding=utf-8

import csv

file_1 = open(r'C:\Users\Administrator\PycharmProjects\data\repository_test02.csv', 'r')
list_1 = csv.reader(file_1)
for row, pars in enumerate(list_1):
    # 从第二行开始取数据
    if row >= 1:
        category = pars[0].decode('gb2312')
        start_time = pars[1].decode('gb2312')
        end_time = pars[2].decode('gb2312')
        describe = pars[3].decode('gb2312')

file_1.close()