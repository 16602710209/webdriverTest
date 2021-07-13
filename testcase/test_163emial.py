import pytest

from pageobject.login import Login
from pageobject.setting import Setting

lg = Login()
st = Setting()


class TestCase():

    def test_mail_001(self, driver):

        """163邮箱登录"""
        lg.login(driver, "13720187233", "zh900209")
        lg.is_login_ok(driver, "张浩")


    @pytest.mark.usefixtures('init_fun')
    def test_mail_002(self, driver):
        """新增签名"""
        st.set_sign(driver, "123", "123456789")
        st.is_add_sign_ok(driver, "123456789")





