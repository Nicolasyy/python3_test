#!/usr/bin/python2
# coding=utf-8

import parameters
from page import base_page
import unittest
import time


class Test_2(unittest.TestCase):
    exe = base_page.Exebasepage()

    def tearDown(self):
        self.exe.refresh()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.exe.closeBrowser()

    def test_login(self):
        self.exe.login('dev', 'admin', '123')
        # 验证登录是否成功
        text1 = self.exe.getText('/html/body/div[1]/ul/li[1]/a')
        print(text1)
        self.assertEqual(text1, u"首页", u"登录失败")
        self.exe.iframe_back()

    def test_add_user(self):
        exe = self.exe
        # 用户信息
        exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[1]/ul/li[1]/a')
        # 新增按钮
        exe.new_add()
        time.sleep(2)
        exe.iframe_second()
        time.sleep(1)
        # 姓名
        exe.sendkeys('i,ui_0_user_name', parameters.add_user.username)
        # 出生日期
        exe.sendkeys('i,ui_0_birthday', parameters.add_user.date)
        # 密码
        exe.sendkeys('i,ui_0_password', parameters.add_user.password)
        # 手机号码
        exe.sendkeys('i,ui_0_mobile_phone', parameters.add_user.phone)
        # 部门
        exe.single_demand('i,ui_0_dept_id_btn', parameters.add_user.department)
        # 岗位
        exe.double_demand('i,ui_0_post_id_btn', parameters.add_user.post)
        exe.save()
        exe.close()
        exe.click('/html/body/div[1]/div[2]/div[1]/dl/dd[1]/ul/li[1]/a')
        time.sleep(1)
        exe.iframe_mainFrame()
        text1 = exe.getText('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[2]')
        userid = exe.getText('/html/body/div[2]/div[4]/div[1]/div/div/div[2]/table/tbody/tr[1]/td[1]')
        print(userid)
        self.assertEqual(text1, parameters.common.username, '创建失败')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    a = [Test_2('test_login'), Test_2('test_add_user')]
    suite.addTests(a)
    unittest.TextTestRunner().run(suite)
