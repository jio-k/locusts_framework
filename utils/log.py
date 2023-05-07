#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
import os

from utils.setting import REPORT_PATH


class Log(object):
    """封装后的logging"""

    def __init__(self, logger=None, log_cate='time_out_log'):
        """指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中"""

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件

        if not os.path.exists(REPORT_PATH):
            os.mkdir(REPORT_PATH)
        self.log_path = REPORT_PATH
        self.log_name = self.log_path + "/" + log_cate + '.log'

        fh = logging.FileHandler(self.log_name, 'w', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            f"{'*' * 10} "
            "%(asctime)s | - "
            "%(filename)s - "
            f"[line:%(lineno)d] {'*' * 10}\n\n"
            "%(message)s\n\n\n"
            f"{'-' * 120}",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
