import pytest

from pageobject.login import Login
from pageobject.setting import Setting
from pageobject.api_renrentest import Login as RRLogin
from pageobject.qqEmail_login import QQEmail_login
from pageobject.qqtalk_0625 import TestQQTalk


lg = Login()
st = Setting()
rr = RRLogin()
qe = QQEmail_login()
qqtalk = TestQQTalk()


@pytest.fixture(scope="function")
def init_fun(driver):
    """163邮箱登录装饰器"""
    lg.login(driver, "13720187233", "zh900209")
    yield
    st.dele_sign(driver)

@pytest.fixture(scope="function")
def login_renren():
    """人人网登录装饰器"""
    da = rr.renren_login("13720187233", "e914aa7b5a650909500c2425d131681b")
    print(da['data']['userName'])
    yield


@pytest.fixture(scope="function")
def qqEmail(driver):
    """QQ邮箱登录装饰器"""
    qe.qqemail_login(driver, "346639189", "qqmima123")
    qe.qqemail_login_ok(driver, "346639189")
    yield

@pytest.fixture(scope="function")
def qqlogin():
    """QQ登录装饰器"""
    qqtalk.test_qqlogin("2490158860", "qqmima123")
    yield

@pytest.fixture(scope="function")
def qqsousuo():
    """QQ搜索好友装饰器"""
    qqtalk.test_qqtalk("牧木")
    yield