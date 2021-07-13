import time
from common.webbase import WebBase
from common.logger import Logger
from common.globalmanager import get_locator_info


log = Logger('web_page.py').getLogger()
locator = get_locator_info()


loc_username = ("id", "username")
loc_psw = ("id", "password")
loc_loginbtn = ("xpath", ".//div[@class='btn-content']/a[@class='btn-login']")


class WebPage(WebBase):

    # def __init__(self, driver):
    #     super(LoginPage,self).__init__(driver)
    #     self.driver = driver


    def loginfun(self, host, username="admin", psw="123ABCdef*"):
        '''敏感信息管理端登录，默认baomi角色'''
        self.driver.maximize_window()
        self.driver.get(host + "/core/login?sys_code=itx&single_mode=itx&login_style=single_sys_info&sys_name=%E5%9F%BA%E7%A1%80%E5%B9%B3%E5%8F%B0&user=&tab_name_show=")
        self.sendKeys(loc_username, username)
        self.sendKeys(loc_psw, psw)
        self.click(loc_loginbtn)
        log.info("登陆成功")


    def web_check(self,result):
        '''主机审核result="1"审核通过；result="0"审核不通过'''
        log.info("-----主机审核开始-----")
        self.web_hostlist()
        self.switch_iframe("rightMain")
        self.click(locator["company"])#点击单位
        self.click(locator["loc_stat"])#点击安装状态
        self.click(locator["installStatus"])#点击安装状态
        self.click(locator["loc_select"])#点击查询
        time.sleep(1)
        self.click(locator["firstData"])#点击第一条数据
        self.move_to_element(locator["hostAct"])#鼠标悬停主机激活
        if result == '1':
            self.click(locator["data1"])  # 点击第一条数据
        elif result == '0':
            self.click(locator["data2"])  # 点击第一条数据
        else:
            print("没有此操作")
        self.click(locator["quedingBtn"])#点击确定
        self.switch_iframe_out()
        log.info("-----主机审核结束-----")

    def web_hostlist(self):
        '''点击主机列表'''
        log.info("-----点击主机列表开始-----")
        self.click(locator["loc_hostgl"])
        self.click(locator["loc_hostlist"])
        log.info("-----点击主机列表结束-----")

    def web_hostcancellist(self):
        '''注销主机列表'''
        log.info("-----注销主机列表开始-----")
        self.click(locator["loc_hostgl"])
        self.click(locator["loc_hostcancel"])
        log.info("-----注销主机列表结束-----")

    def web_hostsele(self):
        '''查询正常记录'''
        log.info("-----查询正常记录开始-----")
        self.switch_iframe("rightMain")
        time.sleep(1)
        self.click(locator["loc_stat"])#点击安装状态
        self.click(locator["loc_normal"])#选择正常
        self.click(locator["loc_select"])#点击查询
        time.sleep(1)
        cancel_code = self.get_text(locator["loc_outcode"])
        user = self.get_text(locator["loc_hostusername"])
        log.info("-----查询正常记录结束-----")
        log.info("获取的注销码为：%s"%cancel_code)
        return cancel_code,user






if __name__ == "__main__":
    ''''''