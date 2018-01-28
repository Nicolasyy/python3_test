#!/usr/bin/python2
# coding=utf-8
import os
import time


def verify(poll, timeout, file_address):
    end_time = time.time() + timeout
    while True:
        value = os.path.exists(file_address)
        if value:
            return value
        time.sleep(poll)
        if time.time() > end_time:
            print('超时,查询不到')
            break