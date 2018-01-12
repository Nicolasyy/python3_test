#!/usr/bin/python2
# coding=utf-8

import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from testcase.quick_check import colors

time_now = time.strftime("%m.%d", time.localtime())
file_1 = open('D:\\click\\parameter.csv', 'r')
list_1 = csv.reader(file_1)
mkpath = "d:\\click\\error\\"
stat_time = time.time()
for pars in list_1:
    url = pars[0]
    ten_id = pars[1]
    username1 = pars[2]
    password1 = pars[3]
    lang = pars[4]
    print(url, ten_id, username1, password1, lang)
    # 干掉谷歌浏览器状态栏提示
    option = webdriver.ChromeOptions()
    option.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(1.5)
    driver.get(url)
    # 企业ID
    driver.find_element_by_id("txtTenantId").send_keys(ten_id)
    # 账号
    driver.find_element_by_id("txtLoginName").send_keys(username1)
    # 密码
    driver.find_element_by_id("txtPassword").send_keys(password1)
    # 选择语言
    s1 = Select(driver.find_element_by_id('lang'))
    s1.select_by_visible_text(lang)
    # 登录
    time.sleep(1)
    driver.find_element_by_id("btnLogin").click()
    time.sleep(1)
    # 登录页面，登录失败打印提示
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/i/a')
    except:
        print('登录失败，请重新尝试')
    else:
        print('登录成功')
    driver.find_elements_by_xpath('//dd[1]/ul[@class="menuson"]/li/a')
    first_list = driver.find_elements_by_xpath('//dd[1]/ul[@class="menuson"]/li/a')
    # 调用函数
    # file_name = mkdir(mkpath)
    # 第一列菜单做特殊处理，单独遍历
    for element_1 in first_list:
        menu1 = element_1.text
        # print menu1
        error_file1 = mkpath + time_now + '.' + ten_id + '.' + menu1 + '.png'
        element_1.click()
        frame_value = driver.find_element_by_id('mainFrame')
        driver.switch_to.frame(frame_value)
        # 第一层判断菜单是否报错
        try:
            # 当前位置
            location1 = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
            driver.switch_to.default_content()
            if menu1 != location1:
                ja = 'window.scroll(0,0)'
                driver.execute_script(ja)
                driver.get_screenshot_as_file(error_file1)
                # print u'\033[31m%s \033[0m不匹配，已截图' %menu1
                # print u'%s' % menu1
                print('%s-与当前位置不匹配' % colors.printRed(menu1))
                continue
        except:
            driver.switch_to.default_content()
            ja = 'window.scroll(0,0)'
            driver.execute_script(ja)
            driver.get_screenshot_as_file(error_file1)
            # print u'\033[31m%s \033[0m不匹配，已截图' %menu1
            # print u'%s' % menu1
            print('%s-页面报错' % colors.printRed(menu1))
            continue
        # 第二层判断是否有添加按钮，打开是否报错
        try:
            frame_value = driver.find_element_by_id('mainFrame')
            driver.switch_to.frame(frame_value)
            # 添加按钮
            add = driver.find_element_by_id('btnAdd')
        except:
            driver.switch_to.default_content()
            continue
        try:
            add.click()
            driver.switch_to.default_content()
            text_1 = driver.find_element_by_xpath('html/body/div[5]/div[1]').text
            driver.find_element_by_xpath('html/body/div[5]/span/a[3]').click()
            if text_1 != location1:
                ja = 'window.scroll(0,0)'
                driver.execute_script(ja)
                driver.get_screenshot_as_file(error_file1)
                # print u'\033[31m%s \033[0m不匹配，已截图' %menu1
                # print u'%s' % menu1
                print('%s-新增页面不匹配' % colors.printRed(menu1))
        except:
            ja = 'window.scroll(0,0)'
            driver.execute_script(ja)
            driver.get_screenshot_as_file(error_file1)
            # print u'\033[31m%s \033[0m不匹配，已截图' %menu1
            # print u'%s' % menu1
            print('%s-新增页面报错' % colors.printRed(menu1))
    # 获取第二栏及后面菜单
    second_list = driver.find_elements_by_xpath('//dl[@class="leftmenu"]/dd/div')
    for element_2 in second_list[1:]:
        # driver.execute_script("arguments[0].scrollIntoView();", element_2)
        try:
            element_2.click()
        except:
            ja = 'window.scroll(0,500)'
            driver.execute_script(ja)
            element_2.click()
            ja = 'window.scroll(0,0)'
        time.sleep(1)
        # 获取子菜单
        bb = '//dd/ul[@class="menuson"and@style="display: block;"]/li/a'
        third_list = driver.find_elements_by_xpath(bb)
        for element_3 in third_list:
            # 元素不可见跳过
            # if not element_3.is_displayed():
            #     continue
            menu2 = element_3.text
            error_file2 = mkpath + time_now + '.' + ten_id + '.' + menu2 + '.png'
            if menu2 == u'课程分类' or menu2 == u'公司档案' or menu2 == u'职位管理' or menu2 == u'部门':
                try:
                    element_3.click()
                except:
                    ja = 'window.scroll(0,700)'
                    driver.execute_script(ja)
                    element_3.click()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                frame_value = driver.find_element_by_id('mainFrame')
                driver.switch_to.frame(frame_value)
                try:
                    # 当前位置
                    location2 = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
                    driver.switch_to.default_content()
                    if menu2 != location2:
                        ja = 'window.scroll(0,0)'
                        driver.execute_script(ja)
                        driver.get_screenshot_as_file(error_file2)
                        # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                        # print u'%s' % menu2
                        print('%s-与当前位置不匹配' % colors.printRed(menu2))
                except:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                    # print u'%s' % menu2
                    print('%s-页面报错' % colors.printRed(menu2))
            elif menu2 == u'课程管理':
                try:
                    element_3.click()
                except:
                    ja = 'window.scroll(0,700)'
                    driver.execute_script(ja)
                    element_3.click()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                frame_value = driver.find_element_by_id('mainFrame')
                driver.switch_to.frame(frame_value)
                try:
                    # 当前位置
                    location2 = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
                    driver.switch_to.default_content()
                    if menu2 != location2:
                        ja = 'window.scroll(0,0)'
                        driver.execute_script(ja)
                        driver.get_screenshot_as_file(error_file2)
                        # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                        # print u'%s' % menu2
                        print('%s-与当前位置不匹配' % colors.printRed(menu2))
                        continue
                except:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                    # print u'%s' % menu2
                    print('%s-页面报错' % colors.printRed(menu2))
                    continue
                try:
                    frame_value = driver.find_element_by_id('mainFrame')
                    driver.switch_to.frame(frame_value)
                    add = driver.find_element_by_id('btnAdd')
                except:
                    driver.switch_to.default_content()
                    continue
                try:
                    add.click()
                    # 点击多课件
                    time.sleep(0.5)
                    driver.find_element_by_xpath('html/body/div[10]/div[3]/a[2]').click()
                    driver.switch_to.default_content()
                    text_2 = driver.find_element_by_xpath('html/body/div[5]/div[1]').text
                    driver.find_element_by_xpath('html/body/div[5]/span/a[3]').click()
                    if text_2 != location2:
                        ja = 'window.scroll(0,0)'
                        driver.execute_script(ja)
                        driver.get_screenshot_as_file(error_file2)
                        # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                        # print u'%s' % menu2
                        print('%s-新增页面不匹配' % colors.printRed(menu2))
                except:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                    # print u'%s' % menu2
                    print('%s-新增页面报错' % colors.printRed(menu2))
            else:
                try:
                    element_3.click()
                except:
                    ja = 'window.scroll(0,700)'
                    driver.execute_script(ja)
                    element_3.click()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                frame_value = driver.find_element_by_id('mainFrame')
                driver.switch_to.frame(frame_value)
                try:
                    # 当前位置
                    location2 = driver.find_element_by_xpath('//ul[@class="placeul"]/li[2]/a').text
                    driver.switch_to.default_content()
                    if menu2 != location2:
                        ja = 'window.scroll(0,0)'
                        driver.execute_script(ja)
                        driver.get_screenshot_as_file(error_file2)
                        # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                        # print u'%s' % menu2
                        print('%s-与当前位置不匹配' % colors.printRed(menu2))
                        continue
                except:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                    # print u'%s' % menu2
                    print('%s-页面报错' % colors.printRed(menu2))
                    continue
                try:
                    frame_value = driver.find_element_by_id('mainFrame')
                    driver.switch_to.frame(frame_value)
                    add = driver.find_element_by_id('btnAdd')
                except:
                    driver.switch_to.default_content()
                    continue
                try:
                    add.click()
                    driver.switch_to.default_content()
                    text_2 = driver.find_element_by_xpath('html/body/div[5]/div[1]').text
                    driver.find_element_by_xpath('html/body/div[5]/span/a[3]').click()
                    if text_2 != location2:
                        ja = 'window.scroll(0,0)'
                        driver.execute_script(ja)
                        driver.get_screenshot_as_file(error_file2)
                        # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                        # print u'%s' % menu2
                        print('%s-新增页面不匹配' % colors.printRed(menu2))
                except:
                    driver.switch_to.default_content()
                    ja = 'window.scroll(0,0)'
                    driver.execute_script(ja)
                    driver.get_screenshot_as_file(error_file2)
                    # print u'\033[31m%s \033[0m不匹配，已截图' %menu2
                    # print u'%s' % menu2
                    print('%s-新增页面报错' % colors.printRed(menu2))
    driver.quit()
    time.sleep(1)
end_time = time.time()
times = end_time - stat_time

file_1.close()
print('总共用时:{:.0f}秒'.format(times))
print('截图地址为：%s' % mkpath)
input()
