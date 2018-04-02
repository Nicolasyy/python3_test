#!/usr/bin/python2
# coding=utf-8

# https://test.exexm.com/SysHome
# https://admin.exexm.com/SysHome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from parameters.path import path
from config import config


class Exebasepage(object):
    c = config.Config()
    p = path.Path().get('common')
    # 干掉谷歌浏览器状态栏提示
    option = webdriver.ChromeOptions()
    # option.add_argument("disable-infobars")
    # option.add_argument("headless")
    # option.add_argument("disable-gpu")
    # argument = ["disable-infobars", "headless", "disable-gpu"]
    # option.add_argument(argument)
    # 指定下载地址，不弹窗
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
    option.add_experimental_option('prefs', prefs)

    def __init__(self, driver=webdriver.Chrome(chrome_options=option)):
        self.driver = driver

    def getElement(self, selector):

        """
        获取元素 getElement('i,aa')
        """
        if selector[1] != ',':
            return self.driver.find_element_by_xpath(selector)
        selector_by = selector[0]
        selector_value = selector[2:]

        if selector_by == "i":
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p":
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t":
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x":
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s":
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def getElements(self, selector):
        """
        获取一组元素 getElements('i,aa')
        """
        if ',' not in selector:
            return self.driver.find_elements_by_xpath(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i":
            elements = self.driver.find_elements_by_id(selector_value)
        elif selector_by == "n":
            elements = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c":
            elements = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l":
            elements = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p":
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t":
            elements = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x":
            elements = self.driver.find_elements_by_xpath(selector_value)
        elif selector_by == "s":
            elements = self.driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return elements

    def click(self, selector):
        el = self.getElement(selector)
        el.click()

    def sendkeys(self, selector, *value):
        el = self.getElement(selector)
        el.send_keys(*value)

    def getText(self, selector):
        el = self.getElement(selector)
        return el.text

    def clear(self, selector):
        clear = self.getElement(selector)
        clear.clear()

    def closeBrowser(self):
        self.driver.close()

    def quitBrowser(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def iframe(self, frame):
        frame_value = self.getElement(frame)
        self.driver.switch_to.frame(frame_value)

    def cut_iframe(self):
        self.driver.switch_to.parent_frame()

    def iframe_back(self):
        self.driver.switch_to.default_content()

    def iframe_mainFrame(self):
        self.iframe(self.p.get('mainframe'))

    def iframe_second(self):
        self.iframe(self.p.get('second_frame'))

    def iframe_third(self):
        self.iframe(self.p.get('third_frame'))

    def arise_wait(self, selector):
        """
        元素出现
        :param selector:
        :return:
        """
        if ',' not in selector:
            return WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, selector)),
                                                        'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, selector_value)),
                                                 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, selector_value)),
                                                 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)),
                                                 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_value)),
                                                 'error')

    def visibility_wait(self, selector):
        """
        元素可见
        :param selector:
        :return:
        """
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, selector)), 'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, selector_value)),
                                                 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, selector_value)),
                                                 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)),
                                                 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_value)),
                                                 'error')

    def click_wait(self, selector):
        """
        元素可点击
        :param selector:
        :return:
        """
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, selector)), 'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, selector_value)), 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, selector_value)), 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, selector_value)),
                                                 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector_value)), 'error')

    def frame_wait(self, selector):
        """
        进入frame
        :param selector:
        :return:
        """
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector)),
                                                        'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, selector_value)),
                                                 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, selector_value)),
                                                 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, selector_value)), 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.LINK_TEXT, selector_value)), 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.PARTIAL_LINK_TEXT, selector_value)), 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector_value)),
                                                 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, selector_value)), 'error')

    def login(self):
        """
        登录操作
        :param TenantId:企业ID
        :param username:用户名称
        :param password: 密码
        """
        # self.driver.set_window_size(1920,1080)
        self.driver.maximize_window()
        self.driver.get(self.c.get('url'))
        self.driver.implicitly_wait(5)
        # 企业ID
        self.sendkeys(self.p.get('tenantId'), self.c.get('tenantId'))
        # 确定
        self.click(self.p.get('confirm'))
        # 账号
        self.sendkeys(self.p.get('userId'), self.c.get('userId'))
        # 密码
        self.sendkeys(self.p.get('password'), self.c.get('password'))
        # 登录
        time.sleep(1)
        self.click(self.p.get('login'))

    def new_add(self):
        """
        新增按钮
        """
        self.iframe_mainFrame()
        self.click(self.p.get('btnAdd'))
        self.iframe_back()

    def double_demand(self, id, value):
        """
        查询1（有两个查询条件）
        :param id:搜索按钮id值
        :param value:搜索名称
        """
        # 搜索ID
        self.getElement(id).click()
        self.iframe_back()
        self.iframe_third()
        # 名称或编号查询
        self.sendkeys(self.p.get('cond_name'), value)
        self.click(self.p.get('btnQuery'))
        time.sleep(1)
        texts = self.getElements(self.p.get('gridResult'))
        for text1 in texts:
            if text1.text == value:
                text1.click()
                break
        time.sleep(1)
        self.click(self.p.get('btnSelectorReturn'))
        self.iframe_back()
        self.iframe_second()

    def single_demand(self, id, value):
        """
        查询2（只有一个查询条件）
        :param id:搜索按钮id值
        :param value:搜索名称
        """
        time.sleep(1)
        # 搜索ID
        self.getElement(id).click()
        self.iframe_back()
        self.iframe_third()
        # 名称或编号查询
        self.sendkeys(self.p.get('txtid'), value)
        self.click(self.p.get('btnQuery'))
        time.sleep(1)
        texts = self.getElements(self.p.get('treeview'))
        for text1 in texts:
            if text1.text == value:
                text1.click()
                break
        self.click(self.p.get('btnSelectorReturn'))
        self.iframe_back()
        self.iframe_second()

    # def search(self, selector, value):
    #     """
    #     查询按钮（部门，岗位，职位，标签，用户）
    #     :param selector:定位元素的值
    #     :param value:查询的值
    #     :return:
    #     """
    #     self.arise_wait(selector)
    #     self.sendkeys(selector, value)
    #     self.sendkeys(selector, Keys.ENTER)

    # def search1(self, selector, value):
    #     """
    #     查询按钮（标签）
    #     :param selector:定位元素的值
    #     :param value:查询的值
    #     :return:
    #     """
    #     self.sendkeys(selector, value)
    #     time.sleep(0.5)
    #     texts = self.getElements('t,li')
    #     for text1 in texts:
    #         if text1.text == value:
    #             text1.click()

    def validity(self, start_time, finish_time):
        """
        有效期
        :param start_time: 开始时间 2010-5-9
        :param finish_time: 结束时间 2010-5-10
        :return:
        """
        self.sendkeys(self.p.get('ui_0_expire_from'), start_time)
        self.sendkeys(self.p.get('ui_0_expire_to'), finish_time)

    def save(self):
        """
        保存按钮
        """
        self.click(self.p.get('btnSave'))

    def close(self):
        """
        关闭
        """
        self.iframe_back()
        self.click(self.p.get('close'))

    def publish(self):
        """
        发布和关闭按钮
        """
        self.click(self.p.get('btnLibPublish'))
        # 确定按钮
        self.click(self.p.get('btnConfirm'))
        self.click_wait(self.p.get('btnAdd'))
        self.close()

    def screenshot(self, filename):
        """
        截图
        :param filename: 文件名字地址
        """
        self.iframe_back()
        ja = 'window.scroll(0,0)'
        self.driver.execute_script(ja)
        self.driver.get_screenshot_as_file(filename)

    # def value(self, selector1, selector2, value):
    #     """
    #     输入数值
    #     :param selector1: 元素1
    #     :param selector2: 元素2
    #     :param value: 输入的数值
    #     :return:
    #     """
    #     self.sendkeys(selector1, "Keys.CONTROL, 'a'")
    #     self.sendkeys(selector2, value)

    def add_photo(self, photo_file):
        """
        上传图片
        :param photo_file: 图片地址
        :return:
        """
        # 上传课程封面
        self.click(self.p.get('btnUploadImage'))
        time.sleep(1)
        self.iframe_back()
        self.iframe_third()
        # 选择图片路径
        self.sendkeys(self.p.get('filePicker'), photo_file)
        # 开始上传
        self.click(self.p.get('upload'))
        self.visibility_wait(self.p.get('btnConfirm'))
        # 确定
        self.click(self.p.get('btnConfirm'))
        self.iframe_back()
        self.iframe_second()

    # def demand(self, selector, value):
    #     self.sendkeys(selector, value)
    #     time.sleep(1)
    #     texts = self.getElements('t,td')
    #     for text1 in texts:
    #         if text1.text == value:
    #             text1.click()
    def dropdown(self, selector1, selector2, value):
        """
        下拉查询框
        :param selector1: 查询框的元素
        :param selector2: 下拉框里面的元素
        :param value: 输入值
        :return:
        """
        aa = 0
        self.sendkeys(selector1, value)
        self.visibility_wait(selector2)
        texts = self.getElements(selector2)
        for text1 in texts:
            if text1.text == value:
                aa = texts.index(text1)
        texts[aa].click()

    def department(self, value):
        """
        部门
        :param value:部门名称
        :return:
        """
        selector1 = '//select[@id="ui_0_target_depts"]/../span/span/span/ul/li/input'
        selector2 = '//ul[@id="select2-ui_0_target_depts-results"]/li/div/span[2]'
        self.dropdown(selector1, selector2, value)

    def dept_label(self, value):
        """
        部门标签
        :param value:部门标签名称
        :return:
        """
        selector1 = '//ul[@id="ui_0_dept_tags_taglist"]/../input'
        selector2 = '//ul[@id="ui_0_dept_tags_listbox"]/li'
        self.dropdown(selector1, selector2, value)

    def post(self, value):
        """
        岗位
        :param value: 岗位名称
        :return:
        """
        selector1 = '//select[@id="ui_0_target_posts"]/../span/span/span/ul/li/input'
        selector2 = '//ul[@id="select2-ui_0_target_posts-results"]/li/div/span[2]'
        self.dropdown(selector1, selector2, value)

    def position(self, value):
        """
        职位
        :param value: 职位名称
        :return:
        """
        selector1 = '//select[@id="ui_0_target_positions"]/../span/span/span/ul/li/input'
        selector2 = '//ul[@id="select2-ui_0_target_positions-results"]/li/div/span[2]'
        self.dropdown(selector1, selector2, value)

    def label(self, value):
        """
        标签
        :param value:标签名称
        :return:
        """
        selector1 = '//ul[@id="ui_0_target_tags_taglist"]/../input'
        selector2 = '//ul[@id="ui_0_target_tags_listbox"]/li'
        self.dropdown(selector1, selector2, value)

    # 要修改
    def user(self, value):
        """
        用户
        :param value: 用户名称
        :return:
        """
        selector1 = '//select[@id="ui_0_target_users"]/../span/span/span/ul/li/input'
        selector2 = '//ul[@id="select2-ui_0_target_users-results"]/li/div/span[2]'
        self.dropdown(selector1, selector2, value)

    def next_step(self):
        """
        下一步
        :return:
        """
        self.click_wait('//li[@class="next"]/a')
        self.click('//li[@class="next"]/a')

    def dropdown_blue(self, selector, value):
        """
        下拉查询框（蓝色版）
        :param selector:框元素值
        :param value:输入值
        :return:
        """
        selector2 = '//div[@class="adropdown highlight"]/table/tbody/tr/td[3]'
        aa = 0
        time.sleep(1)
        self.sendkeys(selector, value)
        time.sleep(1)
        texts = self.getElements(selector2)
        for text1 in texts:
            if text1.text == value:
                aa = texts.index(text1)
        texts[aa].click()

    def people_management(self):
        """
        人员管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[2]/div')

    def learning_management(self):
        """
        学习管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[2]/div')

    def examination_management(self):
        """
        考试管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[3]/div')

    def competency_management(self):
        """
        胜任力管理菜单
        :return:/html/body/div[1]/div[2]/div[1]/dl/dd[9]/div
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[4]/div')

    def knowledge_management(self):
        """
        知识管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[5]/div')

    def message_center(self):
        """
        消息中心菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[6]/div')

    def operations_management(self):
        """
        运营管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[7]/div')

    def work_management(self):
        """
        工作管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[9]/div')

    def product_management(self):
        """
        产品管理菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[10]/div')

    def organization_chart(self):
        """
        组织架构菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[10]/div')

    def report_center(self):
        """
        报表中心菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[12]/div')

    def system(self):
        """
        系统菜单
        :return:
        """
        return self.click('/html/body/div[1]/div[2]/div[1]/dl/dd[13]/div')

    def credit(self, value):
        """
        学分
        :param value:学分值
        :return:
        """
        self.sendkeys('//input[@id="ui_0_score"]/../input[1]', Keys.CONTROL, 'a')
        self.sendkeys('i,ui_0_score', value)

    def integral(self, value):
        """
        积分
        :param value:积分值
        :return:
        """
        self.sendkeys('//input[@id="ui_0_bonus_point"]/../input[1]', Keys.CONTROL, 'a')
        self.sendkeys('i,ui_0_bonus_point', value)

    def electives(self):
        """
        选修对象
        :return:
        """
        self.visibility_wait('//div[@id="target_div"]/span/span/span[2]')
        self.click('//div[@id="target_div"]/span/span/span[2]')
        time.sleep(0.5)
        self.click('//ul[@id="ui_0_target_listbox"]/li[3]')



