from common.webbase import WebBase
from common.globalmanager import get_locator_info


webInfo = get_locator_info()

class QQEmail_write():
    def qqemail_write(self, driver, addressee, title, text_body):
        """写邮件保存在草稿箱"""
        web = WebBase(driver)
        web.click(webInfo['qqemail_write'])
        web.switch_iframe(webInfo['qqemail_write_frame'])
        web.sendKeys(webInfo['qqemail_write_addressee'], addressee)
        web.sendKeys(webInfo['qqemail_write_title'], title)
        web.switch_iframe(webInfo['qqemail_write_text_frame'])
        web.sendKeys(webInfo['qqemail_write_text_body'], text_body)
        web.switch_iframe_up()
        #web.switch_iframe(webInfo['qqemail_write_frame'])
        web.click(webInfo['qqemail_savebtn'])

    def qqemail_write_ok(self, driver, title):
        """验证邮件是否保存成功"""
        web = WebBase(driver)
        web.switch_iframe_out()
        web.click(webInfo['qqemail_caogaoxiang'])
        web.switch_iframe(webInfo['qqemail_caogaoxiang_frame'])
        assert web.get_text(webInfo['qqemail_caogaoxiang_title']) == title

