# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from locust import HttpUser
from locust.contrib.fasthttp import FastHttpUser
from locust import SequentialTaskSet


class LocustOperation(HttpUser):
    abstract = True

    @property
    def user_count(self):
        return self.environment.runner.user_count

    @property
    def web_host(self):
        web_host = self.environment.web_ui.server.server_host
        return 'localhost' if web_host == '::' else web_host

    @property
    def web_port(self):
        return self.environment.web_ui.server.server_port

    def stop_web(self):
        r = requests.get(url=f"http://{self.web_host}:{self.web_port}/stop")
        assert r.status_code == 200

    def stop_headless(self):
        self.environment.runner.quit()

    def stop_load_test(self):
        """停止负载测试"""

        if self.environment.parsed_options and self.environment.parsed_options.headless:
            self.stop_headless()
        else:
            self.stop_web()

    def download_charts_report(self, filepath):
        r = requests.get(url=f"http://{self.web_host}:{self.web_port}/stats/report?download=1")
        assert r.status_code == 200

        with open(filepath, 'wb') as f:
            f.write(r.content)

    def _locust_send(self, request_method, **kwargs):
        return getattr(self.client, request_method.replace('locust_', ''))(**kwargs)


class FastLocustOperation(FastHttpUser):
    abstract = True

    @property
    def user_count(self):
        return self.environment.runner.user_count

    @property
    def web_host(self):
        web_host = self.environment.web_ui.server.server_host
        return 'localhost' if web_host == '::' else web_host

    @property
    def web_port(self):
        return self.environment.web_ui.server.server_port

    def stop_web(self):
        r = requests.get(url=f"http://{self.web_host}:{self.web_port}/stop")
        assert r.status_code == 200

    def stop_headless(self):
        self.environment.runner.quit()

    def stop_load_test(self):
        """停止负载测试"""

        if self.environment.parsed_options and self.environment.parsed_options.headless:
            self.stop_headless()
        else:
            self.stop_web()

    def download_charts_report(self, filepath):
        r = requests.get(url=f"http://{self.web_host}:{self.web_port}/stats/report?download=1")
        assert r.status_code == 200

        with open(filepath, 'wb') as f:
            f.write(r.content)

    def _locust_send(self, request_method, **kwargs):
        kwargs["path"] = kwargs.pop("url")
        response = getattr(self.client, request_method.replace('locust_', ''))(**kwargs)
        response.req = kwargs

        return response


class MyLocustTask(SequentialTaskSet):
    def _locust_send(self, request_method, **kwargs):
        kwargs["path"] = kwargs.pop("url")
        response = getattr(self.client, request_method.replace('locust_', ''))(**kwargs)
        response.req = kwargs

        return response
