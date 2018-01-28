#!/usr/bin/python2
# coding=utf-8

from page.base_page import Exebasepage


class Course(Exebasepage):
    def course_management(self):
        """
        课程管理
        :return:
        """

        self.visibility_wait('/html/body/div[1]/div[2]/div[1]/dl/dd[2]/ul/li[2]/a')
        self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[2]/ul/li[2]/a')

    def courseware_management(self):
        """
        课件管理
        :return:
        """
        self.click("/html/body/div[1]/div[2]/div[1]/dl/dd[2]/ul/li[3]/a")

    def courseware(self):
        """
        单课件
        :return:
        """
        self.iframe_mainFrame()
        self.arise_wait('/html/body/div[9]/div[3]/a[1]')
        self.click('/html/body/div[9]/div[3]/a[1]')
        self.iframe_back()
        self.iframe_second()

    def coursewares(self):
        """
        多课件
        :return:
        """
        self.iframe_mainFrame()
        self.arise_wait('/html/body/div[9]/div[3]/a[2]')
        self.click('/html/body/div[9]/div[3]/a[2]')
        self.iframe_back()
        self.iframe_second()

    def courseware_name(self, value):
        """
        课程名称
        :param value: 课件名称
        :return:
        """
        self.arise_wait('/html/body/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/span/div/input[2]')
        self.dropdown_green('/html/body/div[1]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/span/div/input[2]'
                            , value)

    def course_classification(self, value):
        """
        课程分类
        :param value: 分类名称
        :return:
        """
        self.dropdown_green('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span/div/input[2]'
                            , value)

    def administrative_department(self, value):
        """
        管理部门
        :param value:管理部门名称
        :return:
        """
        self.dropdown_green('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/span/div/input[2]'
                            , value)

    def class_label(self, value):
        """
        课程标签
        :param value:课程标签名称
        :return:
        """
        self.search1('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div/input'
                     , value)

    def learning_period(self, value):
        """
        学习期
        :param value: X天
        :return:
        """
        self.value('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/span/span/input[1]',
                   'i,ui_0_score', value)

    def lecturer(self, value):
        """
        讲师
        :param value:
        :return:
        """
        self.dropdown('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[3]/div/span/span[1]/span/ul/li'
                      '/input', '//ul[@id="select2-ui_0_target_teacher-results"]/li/div/span[2]', value)

    def course_introduction(self, value):
        """
        课程简介
        :param value:
        :return:
        """
        self.sendkeys('i,ui_0_desc', value)

    def credit_setting(self, start, end):
        """
        学分设置
        :param start: 初始学分
        :param end: 结束学分
        :return:
        """
        self.value('/html/body/div[1]/div[2]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/span/span/input[1]',
                   'i,ui_0_begin_score', start)
        self.value('/html/body/div[1]/div[2]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[3]/span/span/input[1]',
                   'i,ui_0_end_score', end)

    def completion_condition(self):
        """
        结业条件-课程学习
        :return:
        """
        self.click('//label[@for="ui_0_pass_by_study"]')
