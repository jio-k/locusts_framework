#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pressure_test
@File ：tools.py.py
@Author ：Ou
@Date ：2022/8/25 16:36
"""
import json
import random
import shutil
import string
from datetime import datetime, timedelta
import time
import zipfile

import os
from pprint import pformat

from utils.setting import LOCUSTS_FRAMEWORK_PATH, BASE_PATH


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_ts_by_days(day=0, hour=0, min=0, seconds=0, milliseconds=0):
    """
    根据当前时间来获取时间戳 例如day=1就是24小时以后的时间戳、day=-1 获取到的就是24小时前的时间戳
    :param day: 天
    :param hour: 时
    :param min: 分
    :param seconds: 秒
    :param milliseconds: 毫秒
    :return:
    """
    time_format = (datetime.now() + timedelta(
        days=day,
        hours=hour,
        minutes=min,
        seconds=seconds,
        milliseconds=milliseconds
    )).strftime("%Y-%m-%d %H:%M:%S")
    time_tuple = time.strptime(time_format, "%Y-%m-%d %H:%M:%S")
    millis = int(time.mktime(time_tuple) * 1000)

    return int(millis)




def get_letter_string(num: int = 8):
    """
    获取一个随机英文字母字符串
    num:字符串数量
    :return:
    """
    letter_str = "testauto" + ''.join(random.sample(string.ascii_lowercase, num))
    return letter_str


def zip_file(filedir):
    """
    压缩文件夹至同名zip文件
    """
    file_news_name = os.path.basename(filedir)
    file_news = filedir + '.zip'
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, filenames in os.walk(filedir):
        f_path = dir_path.replace(filedir, '')
        f_path = f_path and f_path + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    shutil.move(f"{LOCUSTS_FRAMEWORK_PATH}/{file_news_name}.zip", f"{BASE_PATH}/{file_news_name}.zip")


def data_recovery(q):
    """队列处理"""
    el = q.popleft()
    q.append(el)
    return el

def json_format(data, indent=3, width=100):
    """
    把Python字典转换为漂亮的json串
    @param data: json字典
    @param indent: 缩进
    @param width: 宽度
    @return: json串
    """

    data = pformat(data, indent=indent, width=width).replace("'", '"')
    return f"{data}\n"


def print_log(data):
    """格式化json log"""
    try:
        print(json_format(data=data))
    except (IndexError, IndentationError):
        print(data)
