#!/usr/bin/python2
# coding=utf-8

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from page import base_page
import unittest
import time
from parameters import common
from selenium.webdriver.support.ui import WebDriverWait
from parameters import repository_test01

class Test_1(unittest.TestCase):
    exe = base_page.Exebasepage()

    def tearDown(self):
        self.exe.refresh()
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        cls.exe.closeBrowser()

    def test_login(self):
        self.exe.login('dev', 'admin', '123')
        # 验证登录是否成功
        text1 = self.exe.getText('/html/body/div[1]/ul/li[1]/a')
        print text1
        self.assertEqual(text1, u"首页", u"登录失败")
        self.exe.iframe_back()

    def test_1(self):
        # 知识管理
        self.exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/div')
        self.exe.visibility_wait('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/ul/li[4]/a')
        # 知识库
        self.exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/ul/li[4]/a')
        # 新增按钮
        self.exe.new_add()
        self.exe.iframe_second()
        # 知识分类
        self.exe.dropdown_green('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/span/div/input[2]',
                                repository_test01.category)
        # 标题
        self.exe.sendkeys('i,ui_0_title', repository_test01.title)
        # 开放对象
        self.exe.click('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[7]/div/span/span/span[2]')
        time.sleep(1)
        self.exe.click('/html/body/div[8]/div/div[2]/ul/li[2]')
        # 部门
        self.exe.department(repository_test01.department)
        # 岗位
        self.exe.post(repository_test01.post)
        # 职位
        self.exe.position(repository_test01.position)
        # 标签
        self.exe.label(repository_test01.label)
        # 用户
        self.exe.user(repository_test01.username)
        self.exe.iframe('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[13]/div/div/div/div/div[2]/iframe')
        # 输入内容
        self.exe.sendkeys('/html/body', repository_test01.content)
        self.exe.iframe_back()
        self.exe.iframe_second()
        # 上传文件
        self.exe.sendkeys('/html/body/div[1]/div[2]/div[1]/div/div[4]/div[1]/div[1]/div/div/div/div/input',
                          repository_test01.file_name)
        time.sleep(2)
        # 保存
        self.exe.save()
        # 关闭
        self.exe.close()

    def test_2(self):
        # 知识管理
        self.exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/div')
        self.exe.visibility_wait('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/ul/li[3]/a')
        # 知识分类
        self.exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/ul/li[3]/a')
        # 新增
        self.exe.new_add()
        self.exe.iframe_second()
        # 类别名称
        self.exe.sendkeys('i,ui_0_name', 'aa0802')
        # 有效期
        self.exe.validity(common.start_time, common.end_time)
        # 描述
        self.exe.sendkeys('i,ui_0_remark', 'aa')
        self.exe.save()
        self.exe.close()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    a = [Test_1('test_login'), Test_1('test_1')]
    suite.addTests(a)
    unittest.TextTestRunner().run(suite)
