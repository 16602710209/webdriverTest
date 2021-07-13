import time
from common.webbase import WebBase
from common.globalmanager import get_locator_info

webInfo = get_locator_info()

class Setting():
    def set_sign(self, driver, title, content):
        """新增签名的方法"""
        web = WebBase(driver)
        web.click(webInfo['setting'])
        web.click(webInfo['normal_set'])
        time.sleep(2)
        web.click(webInfo['sign'])
        time.sleep(2)
        web.click(webInfo['alertsave'])
        time.sleep(2)
        web.click(webInfo['add_sign'])
        web.sendKeys(webInfo['intitle'], title)
        web.switch_iframe(webInfo['iframe2'])
        web.sendKeys(webInfo['incontent'], content)
        web.switch_iframe_out()
        web.click(webInfo['save'])


    def is_add_sign_ok(self, driver, sign):
        """断言签名是否成功"""
        web = WebBase(driver)
        assert web.get_text(webInfo['is_add_success']) == sign

    def dele_sign(self, driver):
        """删除签名"""
        web = WebBase(driver)
        driver.refresh()
        web.click(webInfo['dele'])
        web.click(webInfo['dele_ok'])
