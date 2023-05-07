#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import subprocess

import sys
from locust import events, LoadTestShape, tag, constant
from locust.user import task

from commom.base import MyLocustTask, FastLocustOperation
from utils.setting import LOCUST_CFG_PATH, REPORT_PATH
from utils.tools import read_json

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

locust_cfg_data = read_json(path=LOCUST_CFG_PATH)

operation_flow = locust_cfg_data["operation_flow"]
failed_durations = locust_cfg_data["failed_durations"]
if failed_durations.strip() == "":
    failed_durations = 10000


def data_recovery(q):
    el = q.popleft()
    q.append(el)
    return el


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("前置方法启动")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')


class Mytask(MyLocustTask):

    def on_start(self):
        print("用户启动！！！！！")

    def on_stop(self):
        print('on_stop')

    @tag(operation_flow)
    @task
    def locust_interface_name_pressure_test(self):
        """写压测接口"""
        pass


class MyCustomShape(LoadTestShape):
    """
            负载模式
            time -- 持续时间,  经过多少秒后,进入到下个阶段
            users -- 总用户数
            spawn_rate -- 产生率,即每秒启动/停止的用户数
    """
    setp_time = locust_cfg_data["setp_time"]
    if setp_time.strip() == "":
        setp_time = 10

    time_limit = locust_cfg_data["time_limit"]
    if time_limit.strip() == "":
        time_limit = 600
    else:
        time_limit = int(time_limit)

    number_of_user = locust_cfg_data["number_of_user"]
    if number_of_user.strip() == "":
        number_of_user = 20

    stages = [
        {"time": int(setp_time), "users": 1, "spawn_rate": 1},
        {"time": int(time_limit), "users": int(number_of_user), "spawn_rate": 30},
    ]

    def tick(self):

        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage['time']:
                tick_data = (stage['users'], stage['spawn_rate'])
                return tick_data

        return None


class QuickstartUser(FastLocustOperation):
    debug_stream = open(os.path.join(REPORT_PATH, "locust_request_log"), "a+")
    wait_time = constant(2)

    # def __init__(self, environment):
    #     super().__init__(environment)

    def on_start(self):
        print("用户启动！！！！！")

    def on_stop(self):
        print('on_stop')

    tasks = [Mytask]


if __name__ == '__main__':
    # 网页模式
    # subprocess.call(locust -f {str(__file__)} --web-port 9090', shell=True)
    name = os.path.basename(__file__).split('.')[0]
    # 无头模式
    subprocess.call(
        f'locust -f {str(__file__)}'
        f'  --tags {operation_flow}'
        f' --csv={REPORT_PATH}/example'
        f' --headless --html={os.path.join(REPORT_PATH, f"{name}.html")}',
        shell=True)
