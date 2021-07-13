import time
from common.webbase import WebBase
from common.globalmanager import get_locator_info

webInfo = get_locator_info()


class Login():

    def login(self, driver, username, psw):

        """这是一个登录方法"""
        web = WebBase(driver)
        driver.get('https://mail.163.com/')
        driver.maximize_window()
        time.sleep(2)
        web.switch_iframe(webInfo['frame'])
        web.sendKeys(webInfo['username'], username)
        web.sendKeys(webInfo['password'], psw)
        web.click(webInfo['login'])

    def is_login_ok(self, driver, username):
        """断言登录成功"""
        web = WebBase(driver)
        assert web.get_text(webInfo['islogin']) == username

