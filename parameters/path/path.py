#!/usr/bin/python3
# coding=utf-8

from config import config
from common.file_reader import YamlReader


class Path(object):
    def __init__(self, path=config.PATH_FILE):
        self.config = YamlReader(path).data
        self.value = None

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(element)






