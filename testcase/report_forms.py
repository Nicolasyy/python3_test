#!/usr/bin/python2
#coding=utf-8

import unittest
import time
from page import base_page
from common import common
from selenium.webdriver.common.keys import Keys


class Test_1(unittest.TestCase):

    report = base_page.Exebasepage()

    def tearDown(self):
        self.report.refresh()
        time.sleep(1)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.report.quitBrowser()

    def test_login(self):
        self.report.login('dev', 'admin', '123')
        text1 = self.report.getText('/html/body/div[1]/ul/li[1]/a')
        self.assertEqual(text1, u"首页", u"登录失败" )
        self.report.iframe_back()

    def test_1(self):
        self.report.system()
        self.report.click(u'l,操作日志')
        self.report.iframe_mainFrame()
        self.report.click('i,btnQuery')
        self.report.arise_wait('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[1]')
        text = self.report.getText('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[1]')
        print(text)
        self.assertIsNotNone(text, u'查询失败')
        self.report.click('i,btnExport')
        file_address = 'D:\\操作日志.csv'
        filename = common.verify(0.5, 65, file_address)
        self.assertTrue(filename, u'不存在')
        aa = self.report.getText(".//*[@id='btnQuery']")
        print(aa)
        handles = self.report.driver.window_handles
        print(handles)
        self.report.driver.switch_to_window(handles[1])
        self.report.closeBrowser()
        self.report.driver.switch_to_window(handles[0])
        # self.report.iframe_back()
        # self.report.click('l,权限设置')

    def test_2(self):
        self.report.report_center()
        time.sleep(1)
        self.report.click(u'l,区域学习状况跟踪表')
        self.report.iframe_mainFrame()
        self.report.click('//*[@id="ui_0_Area_btn"]')
        time.sleep(4)
        self.report.iframe_back()
        self.report.iframe('html/body/div[6]/div[2]/iframe')
        self.report.click("i,gridResult_selected_check")
        self.report.sendkeys("//*[@id='gridResult_selected_check']", Keys.SPACE)
        time.sleep(5)
        self.report.report_center()
        time.sleep(0.5)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    a = [Test_1('test_login'), Test_1('test_2')]
    suite.addTests(a)
    unittest.TextTestRunner().run(suite)








