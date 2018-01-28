#!/usr/bin/python2
# coding=utf-8

from page import base_page
import unittest
import time
from parameters import common
import csv

a = 1

ten_id, username1, password1, n = common.parameter()

class Taa(unittest.TestCase):
        admin = base_page.Exebasepage()
        # 定义要创建的目录
        mkpath = "d:\\error\\"
        # 调用函数
        file_name = common.mkdir(mkpath)

        @classmethod
        def tearDownClass(cls):
            cls.admin.closeBrowser()

        def test_login(self):

            self.admin.login(ten_id, username1, password1)
            # self.admin.login('dev', 'admin', '123')
            # 验证登录是否成功
            self.admin.iframe_mainFrame()
            text1 = self.admin.getText('/html/body/div[1]/ul/li[1]/a')
            print(text1)
            self.assertEqual(text1, "首页", "登录失败")
            self.admin.iframe_back()

        def test_1(self):
            self.admin.driver.implicitly_wait(5)
            # 第一列菜单做特殊处理，单独遍历
            first_list = self.admin.getElements('//dd[1]/ul[@class="menuson"]/li/a')
            for element_1 in first_list:
                text_1 = element_1.text
                print(text_1)
                error_file1 = self.mkpath + common.localtime() + '.' + ten_id + '.' + text_1 + '.png'
                element_1.click()
                self.admin.iframe_mainFrame()
                # 获取不到页面元素，抛异常截图
                try:
                    aa = self.admin.getElement('//ul[@class="placeul"]/li[2]/a').text
                    self.assertIn(text_1[:2], aa)
                except:
                    self.admin.screenshot(error_file1)
                self.admin.iframe_back()
            # 获取菜单
            second_list = self.admin.getElements('//dl[@class="leftmenu"]/dd/div')
            for element_2 in second_list[1:]:
                element_2.click()
                time.sleep(1)
                # 获取子菜单
                third_list = self.admin.getElements('//dd/ul[@class="menuson"]/li/a')
                for element_3 in third_list:
                    # 元素不可见跳过
                    if not element_3.is_displayed():
                        continue
                    text_2 = element_3.text
                    print(text_2)
                    error_file2 = self.mkpath + common.localtime() + '.' + ten_id + '.' + text_2 + '.png'
                    element_3.click()
                    self.admin.iframe_mainFrame()
                    # 获取不到页面元素，抛异常截图
                    try:
                        bb = self.admin.getElement('//ul[@class="placeul"]/li[2]/a').text
                        self.assertIn(text_2[:2], bb)
                    except:
                        self.admin.screenshot(error_file2)
                    self.admin.iframe_back()


if __name__ == "__main__":
        suite = unittest.TestSuite()
        a = [Taa('test_login'), Taa('test_1')]
        suite.addTests(a)
        unittest.TextTestRunner().run(suite)
