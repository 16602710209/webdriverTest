#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from urllib.parse import urljoin,urlencode
import urllib3
from common.logger import Logger
from urllib3.exceptions import InsecureRequestWarning
from common.globalmanager import GlobalManager

logger = Logger('apibase.py').getLogger()


class ApiBase():
    '''接口测试工具类'''

    def __init__(self):
        self.timeout = 10   #接口的超时时间，单位秒
        self.gm = GlobalManager()
        self.gm.set_value('s',requests.session()) #{"s":"requests.session()"}

    def post(self,url,data,json=None,headers=None,cookies=None,files=None):
        '''post请求'''
        logger.info('POST-接口请求地址：{}'.format(url))
        try:
            urllib3.disable_warnings(InsecureRequestWarning) #关闭https告警信息
            res = self.gm.get_value('s').post(url=url,data=data,json=json,files=files,headers=headers,cookies=cookies,timeout=self.timeout,verify=False)
            logger.debug('POST-接口请求总时长，单位秒：{}'.format(res.elapsed.total_seconds()))
            assert res.status_code == 200
            logger.debug('POST-接口的响应码：{}'.format(res.status_code))
            return res
        except Exception as e:
            logger.error('POST-接口请求超时：{}'.format(e))
            return None

    def get(self,url,data=None,headers=None,cookies=None):
        '''get请求'''
        logger.info('GET-接口请求地址：{}'.format(url))
        try:
            urllib3.disable_warnings(InsecureRequestWarning)
            res = self.gm.get_value('s').get(url=url,data=data,headers=headers,cookies=cookies,timeout=self.timeout,verify=False)
            logger.debug('GET-接口请求总时长，单位秒：{}'.format(res.elapsed.total_seconds()))
            assert res.status_code == 200
            logger.debug('GET-接口的响应码：{}'.format(res.status_code))
            return res
        except Exception as e:
            logger.error('GET-接口请求超时：{}'.format(e))
            return None

    def url_join(self, base, url):
        '''拼接url地址'''
        return urljoin(base, url)

    def query_str_join(self,str_dict,url):
        '''拼接查询字符串'''
        query_string = urlencode(str_dict)
        return url + '?' + query_string

    def is_json(self, str):
        try:
            eval(str)
            return True
        except Exception as e:
            logger.debug("非json字符串:{}, error:{}".format(str, e))
            return False

