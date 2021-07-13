import pytest

from pageobject.qqtalk_0625 import TestQQTalk

qtk = TestQQTalk()

class Test_QQTalk():
    def test_qqlogin(self):
        """QQ登录"""
        qtk.test_qqlogin("2490158860", "qqmima123")

    @pytest.mark.usefixtures('qqlogin')
    def test_sousuo(self):
        """QQ搜索好友"""
        qtk.test_qqtalk("牧木")

    @pytest.mark.usefixtures('qqsousuo')
    @pytest.mark.usefixtures('qqlogin')
    def test_sendtext(self):
        qtk.test_qqsend("哈哈哈哈哈哈哈傻子")

