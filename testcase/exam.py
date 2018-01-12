#!/usr/bin/python2
#coding=utf-8

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from page import element
import unittest
import time

element1 = element.Basepage(webdriver.Firefox())
class Test(unittest.TestCase):

    def test_1(self):
        # element1 = element1.Basepage(webdriver.Firefox())
        # profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\hc9mht9x.default'
        # profile = webdriver.FirefoxProfile(profile_directory)
        element1.driver.maximize_window()
        element1.driver.get("https://test.exexm.com/SysHome")
        element1.driver.implicitly_wait(10)
        #企业ID
        element1.id_key("txtTenantId","dev")
        #账号
        element1.id_key("txtLoginName","admin")
        #密码
        element1.id_key("txtPassword","123")
        #登录
        element1.id_click("btnLogin")
        time.sleep(3)
        #验证登录是否成功
        element1.iframe_mainFrame()
        text1 = element1.driver.find_element_by_link_text(u'首页').text
        print text1
        self.assertEqual(text1,u"首页",u"登录失败" )
        element1.iframe_back()


