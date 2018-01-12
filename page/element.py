#!/usr/bin/python2
# coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
now = time.strftime("%m.%d.%H.%M.%S",time.localtime())


class autowebdriver():
    # 干掉谷歌浏览器状态栏提示
    option = webdriver.ChromeOptions()
    option.add_argument("disable-infobars")

    def __init__(self, driver=webdriver.Chrome(chrome_options=option)):
        self.driver = driver

    def getElement(self, selector):
        """
        获取元素 getElement('i,aa')
        """
        if ',' not in selector:
            return self.driver.find_element_by_xpath(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
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

        if selector_by == "i" or selector_by == 'id':
            elements = self.driver.find_elements_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            elements = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            elements = self.driver.find_elements_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            elements = self.driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return elements

    def click(self, selector):
        el = self.getElement(selector)
        el.click()

    def sendkeys(self, selector, value):
        el = self.getElement(selector)
        el.send_keys(value)

    def getText(self, selector):
        el = self.getElement(selector)
        return el.text

    def clear(self, selector):
        clear = self.getElement(selector)
        clear.clear()

    def closeBrowser(self):
        self.driver.close()

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
        self.iframe('i,mainFrame')

    def iframe_second(self):
        self.iframe('/html/body/div[5]/div[2]/iframe')

    def iframe_third(self):
        self.iframe('/html/body/div[7]/div[2]/iframe')

    def arise_wait(self, selector):
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector)), 'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, selector_value)), 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, selector_value)), 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)), 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_value)), 'error')

    def visibility_wait(self, selector):
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, selector)), 'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, selector_value)), 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, selector_value)), 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)), 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector_value)), 'error')

    def click_wait(self, selector):
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
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, selector_value)), 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector_value)), 'error')

    def frame_wait(self, selector):
        if ',' not in selector:
            return WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector)), 'error')
        method = selector.split(',')[0]
        selector_value = selector.split(',')[1]
        if method == "i":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, selector_value)), 'error')
        elif method == "n":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, selector_value)), 'error')
        elif method == "c":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, selector_value)), 'error')
        elif method == "l":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.LINK_TEXT, selector_value)), 'error')
        elif method == "p":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.PARTIAL_LINK_TEXT, selector_value)), 'error')
        elif method == "t":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, selector_value)), 'error')
        elif method == "x":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, selector_value)), 'error')
        elif method == "s":
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, selector_value)), 'error')


