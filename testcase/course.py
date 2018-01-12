#!/usr/bin/python2
# coding=utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from parameters import course_test02
from page import course
import unittest
import time


class Test_1(unittest.TestCase):

    course = course.Course()

    def tearDown(self):
        self.course.refresh()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.course.closeBrowser()

    def test_login(self):
        self.course.login('dev', 'admin', '123')
        # 验证登录是否成功
        # self.course.arise_wait('/html/body/div[1]/ul/li[1]/a')
        # self.course.iframe_mainFrame()
        text1 = self.course.getText('/html/body/div[1]/ul/li[1]/a')
        self.assertEqual(text1, u"首页", u"登录失败" )
        self.course.iframe_back()

    # 课件管理
    def test_1(self):
        # 学习管理
        self.course.learning_management()
        # 课件管理
        self.course.courseware_management()
        # 新增课件
        self.course.new_add()
        self.course.iframe_second()
        # 上传文件
        self.course.add_photo(c)
        # 课件名称
        self.course.clear('i,ui_0_name')
        self.course.sendkeys('i,ui_0_name', parameters.course_test02.courseware_name)
        # 课件时长
        # self.course.clear('i,ui_0_length')
        # self.course.sendkeys('i,ui_0_length', parameters.course.courseware_time)
        # 勾选授权管理员使用
        self.course.click('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[12]/div/label')
        # 部门
        self.course.search('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[13]/div/span/span[1]/span', parameters.common.department)
        # 岗位
        self.course.search('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[14]/div/span/span[1]/span', parameters.common.post)
        # 职位
        self.course.search('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[15]/div/span/span[1]/span', parameters.common.position)
        # 标签
        self.course.search('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[16]/div/div/div/input', parameters.common.label)
        # 添加用户
        self.course.search('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[17]/div/span/span[1]/span', parameters.common.username)
        # 点击保存
        self.course.save()
        time.sleep(2)
        self.course.close()
        # 断言验证
        self.course.click("/html/body/div[1]/div[2]/div[1]/dl/dd[2]/ul/li[3]/a")
        time.sleep(1)
        self.course.iframe_mainFrame()
        text1 = self.course.getText('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[2]')
        print(text1)
        self.assertEqual(text1, parameters.course_test02.courseware_name, u"创建失败" )
        self.course.iframe_back()
        time.sleep(1)

    # 课程管理
    def test_2(self):
        # 学习管理
        self.course.learning_management()
        # 课程管理
        self.course.course_management()
        # 新增课程
        self.course.new_add()
        # 多课件
        self.course.coursewares()
        # 选取课件名称
        self.course.courseware_name(course_test02.courseware_name)
        # 上传图片
        self.course.add_photo(course_test02.courseware_file)
        # 下一步
        self.course.next_step()
        # 课程分类
        self.course.course_classification(course_test02.course_classify)
        # 管理部门
        self.course.administrative_department(course_test02.manage_departmen)
        # 课程标签
        self.course.class_label(course_test02.tag)
        # 学习期
        self.course.learning_period(course_test02.date)
        # 讲师
        self.course.lecturer(course_test02.lecturer)
        # 有效期
        self.course.validity(course_test02.start_time, course_test02.end_time)
        # 课程简介
        self.course.course_introduction(course_test02.intro)
        # 下一页
        self.course.next_step()
        # 选修条件-学分设置
        self.course.credit_setting(course_test02.start_credit, course_test02.end_credit)
        # 结业条件
        self.course.completion_condition()
        # 结业奖励-学分
        self.course.credit(course_test02.credit)
        # 结业奖励-积分
        self.course.integral(course_test02.integral)
        # 下一页
        self.course.next_step()
        # 选修对象
        self.course.electives()
        # 部门
        self.course.department(course_test02.department)
        # 部门标签
        self.course.dept_label(course_test02.tag_department)
        # 岗位
        self.course.post(course_test02.post)
        # 职位
        self.course.position(course_test02.position)
        # 标签
        self.course.label(course_test02.label)
        # 选择用户
        self.course.user(course_test02.usersname)
        self.course.save()
        time.sleep(0.5)
        self.course.publish()
        # 断言验证
        self.course.click("/html/body/div[1]/div[2]/div[1]/dl/dd[2]/ul/li[2]/a")
        self.course.iframe_mainFrame()
        text1 = self.course.getText('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[2]')
        print(text1)
        self.assertEqual(text1, course_test02.courseware_name, "创建失败")
        self.course.iframe_back()

    # 课程分类
    def test_3(self):
        # 学习管理
        self.course.click("/html/body/div[1]/div[2]/div[1]/dl/dd[2]/div")
        time.sleep(1)
        # 课程分类
        self.course.click(u'l,课程分类')
        # 选择课程分类大类
        self.course.iframe_mainFrame()
        self.course.click('/html/body/div[2]/div[1]/div[2]/div/ul/li/div/span[2]')
        self.course.iframe_back()
        # 新增课程分类
        self.course.new_add()
        # 课程名称
        self.course.iframe_mainFrame()
        self.course.sendkeys('i,ui_0_name', parameters.common.course_classification)
        # 课程说明
        self.course.sendkeys('i,ui_0_desc', parameters.course_test02.state)
        self.course.save()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    a = [Test_1('test_login'), Test_1('test_2')]
    suite.addTests(a)
    unittest.TextTestRunner().run(suite)