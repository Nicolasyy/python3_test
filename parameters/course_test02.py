#!/usr/bin/python2
#coding=utf-8


import csv

file_1 = open(r'C:\Users\Administrator\PycharmProjects\data\course_test02.csv', 'r')
list_1 = csv.reader(file_1)
for row, pars in enumerate(list_1):
    if row >= 1:
        # 课件名称
        courseware_name = pars[0]
        # 课件图片地址
        courseware_file = pars[1]
        # 课程分类
        course_classify = pars[2]
        # 管理部门
        manage_departmen = pars[3]
        # 课程标签
        tag = pars[4]
        # 学习期
        date = pars[5]
        # 讲师
        lecturer = pars[6]
        # 有效期
        start_time = pars[7]
        end_time = pars[8]
        # 课程简介
        intro = pars[9]
        # 选修学分
        start_credit = pars[10]
        end_credit = pars[11]
        # 结业条件
        # 课程学习  study
        # 课后考试  exam
        # 课程评价  comment
        # Completion_condition = {'study': '//label[@for="ui_0_pass_by_study"]', 'exam': '//label[@for="ui_0_pass_by_exam"]',
        #                         'comment': '//label[@for="ui_0_pass_by_comment"]'}
        # 学分
        credit = pars[12]
        # 积分
        integral = pars[13]
        # 部门
        department = pars[14]
        # 部门标签
        tag_department = pars[15]
        # 岗位
        post = pars[16]
        # 职位
        position = pars[17]
        # 标签
        label = pars[18]
        # 用户名称
        usersname = pars[19]
file_1.close()
