import pytest
from selenium import webdriver

from common.webbase import WebBase
from pageobject.qqEmail_login import QQEmail_login
from pageobject.qqEmail_write import QQEmail_write
from common.read_excel import ExcelUtil



qel = QQEmail_login()
qew = QQEmail_write()
path = r"C:\\Users\\saloa\\Desktop\\TestDemo\\data\\qqEmail.xls"
xls = ExcelUtil(path)
qqEmaildata =xls.get_xls_data(1)

class TestCase_QQEmail():
    # def setup(self):
    #     self.driver = webdriver.Chrome()

    @pytest.mark.parametrize("qqEmaildata", qqEmaildata)
    def test_qqemail_login(self, driver, qqEmaildata):
        """QQ邮箱登录测试用例"""
        qel.qqemail_login(driver, qqEmaildata['QQ账号'], qqEmaildata['QQ密码'])
        qel.qqemail_login_ok(driver, qqEmaildata['断言'])


    @pytest.mark.usefixtures('qqEmail')
    def test_qqemail_write(self, driver):
        """QQ邮箱写邮件测试用例"""
        qew.qqemail_write(driver, "346639189", "测试2", "写进去了")
        qew.qqemail_write_ok(driver, "测试2")