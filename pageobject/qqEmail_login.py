import time

from selenium import webdriver

from common.webbase import WebBase
from common.globalmanager import get_locator_info

webInfo = get_locator_info()

class QQEmail_login():

    def qqemail_login(self, driver, userid, password):
        """QQ邮箱登录方法"""
        web = WebBase(driver)
        driver.get("https://mail.qq.com/")
        driver.maximize_window()
        time.sleep(2)
        web.switch_iframe(webInfo['qqemail_login_frame'])
        web.sendKeys(webInfo['qqemail_userid'], userid)
        web.sendKeys(webInfo['qqemail_password'], password)
        web.click(webInfo['qqemail_loginbtn'])
        time.sleep(2)

    def qqemail_login_close(self):
        driver.close()

    def qqemail_login_ok(self, driver, userid):
        web = WebBase(driver)
        qqemail = userid + '@qq.com'
        assert web.get_text(webInfo["qqemail_login_ok"]) == qqemail
        driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = WebBase(driver)
    driver.get("https://mail.qq.com/")
    qq = QQEmail_login()
    qq.qqemail_login(driver, "2490158860", "qqmima123")
