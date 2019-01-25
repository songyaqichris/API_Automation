# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py

import sys
from os import path

import allure
import pytest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from Params.params import Login
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestLogin:
    @allure.MASTER_HELPER.feature('Home')
    @allure.MASTER_HELPER.severity('blocker')
    @allure.MASTER_HELPER.story('Login')
    def test_test_01(self, action):
        """
            用例描述：未登陆状态下查看基础设置
        """
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request(action)
        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = req_url + urls[0]
        response = request.get_request(api_url, params[0], headers[0])

        assert test.assert_code(response['code'], 401)
        assert test.assert_body(response['body'], 'error', u'继续操作前请注册或者登录.')
        assert test.assert_time(response['time_consuming'], 100)
        Consts.RESULT_LIST.append('True')

if __name__ == '__main__':
    TestLogin().test_test_01(1)
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Basic')
    # def test_basic_02(self, action):
    #     """
    #         用例描述：登陆状态下查看基础设置
    #     """
    #     conf = Config()
    #     data = Login()
    #     test = Assert.Assertions()
    #     request = Request.Request(action)
    #
    #     host = conf.host_debug
    #     req_url = 'http://' + host
    #     urls = data.url
    #     params = data.data
    #     headers = data.header
    #
    #     api_url = req_url + urls[1]
    #     response = request.post_request(api_url, params[1], headers[1])
    #
    #     assert test.assert_code(response['code'], 401)
    #     assert test.assert_text(response['text'], '{"error":"继续操作前请注册或者登录."}')
    #     Consts.RESULT_LIST.append('True')
