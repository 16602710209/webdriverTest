import os.path

import pytest

from pageobject.api_renrentest import Login
from pageobject.api_renrentest2 import Renren_set
from common.read_yaml import readyml

root_path = os.path.dirname(os.path.dirname(__file__))# 获取项目路径
yaml_path = os.path.join(root_path, 'data', 'caseData.yaml')

lg = Login()
rs = Renren_set()
yaml_info = readyml(yaml_path)['TestCase']


class TestCase():
    @pytest.mark.parametrize('yaml_info_case1', yaml_info['case1'])
    def test_renren_01(self, yaml_info_case1):
        """人人网登陆"""
        res = lg.renren_login(yaml_info_case1['username'], yaml_info_case1['password'])
        assert res['errorMsg'] == "成功"


    @pytest.mark.usefixtures("login_renren")
    def test_renren_02(self):
        """人人网设置"""
        res = rs.set_ziliao()
        print(res)
        assert res == True
