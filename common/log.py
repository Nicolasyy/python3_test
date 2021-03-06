#!/usr/bin/python3

import logging
from logging.handlers import TimedRotatingFileHandler
from config.config import LOG_PATH
from config import config
import os


class Logger(object):
    def __init__(self, logger_name='auto_web'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = config.Config().get('log')
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'
        # if c and c.get('file_name'):
        #     self.log_file_name = c.get('file_name')
        # else:
        #     self.log_file_name = 'test.log'
        self.backup_count = c.get('backup') if c and c.get('backup') else 5  # 保留的日志数量
        # 日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            # 每天重新创建一个日志文件，最多保留backup_count
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when="D",
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

aa = Logger()

def log(msg):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = Logger().get_logger()
            try:
                func(*args, **kwargs)
                logger.info(msg)
            except Exception as e:
                # log the exception
                # err = "There was an exception in "
                # err += func.__name__
                logger.exception(e)

                # re-raise the exception
                raise
        return wrapper
    return decorator


