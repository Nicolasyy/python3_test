#!/usr/bin/python2
# coding=utf-8
import time
import csv

# 用户名称
username = 'zz739'
# 密码
password = 'abc1234'
# 出生日期
date = '2017-06-28'
# 部门
department = '项目一部'
# 岗位
post = '开放对象测试'
# 职位
position = '实习生'
# 标签
label = 'test-2'
# 手机号码
phone = '18750943673'
# 课程分类
course_classification = '测试333'
# 图片地址
file = r'D:\xiazai\apic16935.jpg'
# 有效期
start_time = '2017-6-30'
end_time = '2017-8-30'



def localtime():
    time_now = time.strftime("%m.%d", time.localtime())
    return time_now


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # print path + u'创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print path + u'目录已存在'
        return False


def parameter():
    n = 0
    file_1 = open('D:\\parameter.csv', 'r')
    list_1 = csv.reader(file_1)
    for pars in list_1:
        ten_id = pars[0]
        username1 = pars[1]
        password1 = pars[2]
        n += 1
        return ten_id, username1, password1, n
    print(n)
    file_1.close()

