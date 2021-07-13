import requests
import re
import time
import os
import pickle
from common.logger import Logger
import json
from common.globalmanager import GlobalManager
from common.read_excel import ExcelUtil
from common.config import Config

log = Logger('api_page.py').getLogger()
config = Config.getConfig()

rootPath = GlobalManager().get_value('rootPath')
filePath = os.path.join(rootPath, "config")  # 表格路径
fileupdown = os.path.join(rootPath, "tools")  # 表格路径
Path = os.path.join(filePath, "apidata.xlsx")  # 表格


class ApiDemo():
    def __init__(self):

        self.s = requests.session()
        self.host = "172.168.3.194"
        self.ip = "http://172.168.3.194:8010"
        # self.driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
        # self.driver = webdriver.Chrome()
        self.header1 = {
            "Content-Type": "application/json"
        }
        self.header2 = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

    def get_exl_url(self, row):
        '''获取表格中的URL'''
        data = ExcelUtil(Path)
        testdates = data.get_cellinfo(row,"URL")
        return testdates

    def get_exl_body(self, row):
        '''获取表格中的请求数据'''
        data = ExcelUtil(Path)
        testdates = data.get_cellinfo(row, "请求参数")
        return testdates

    def get_exl_expect(self, row):
        '''获取表格中的预期结果'''
        data = ExcelUtil(Path)
        testdates = data.get_cellinfo(row, "预期结果")
        return testdates

    def get_cookie(self, username, password):  # 初次登录用selenium模拟，并获得cookies
        driver = webdriver.PhantomJS(executable_path=os.path.join(rootPath, config['browser']['exec_path'], "phantomjs.exe"))
        # driver = webdriver.Chrome(executable_path=os.path.join(rootPath, config['browser']['exec_path'], "chromedriver.exe"))
        login_url = "http://"+ self.host + ':8888/core/login'
        # 打开登录页面
        driver.get(login_url)
        print("开始登录......")
        # 向浏览器发送用户名、密码，并点击登录按钮
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath(".//div[@id='user']/following-sibling::div[2]/input").click()
        time.sleep(3)
        print("登陆成功......")
        url = driver.current_url
        cookie = re.findall("session_id=(.*?)&jsuid", url)[0]
        # cookies = driver.get_cookies()
        driver.quit()
        return cookie

    def get_user_cookies(self, username, password):  # 获取session
        '''获取系统当前用户的cookies'''
        if not os.path.exists('cookie_' + username + '.txt'):
            cookie = self.get_cookie(username, password)
            self.save_cookie(username, cookie)
        else:
            cookie = self.load_cookie(username)
        return cookie

    def save_cookie(self, username, cookie):
        with open("cookie_" + username + ".txt", 'wb') as f:
            pickle.dump(cookie, f)
            print("Cookie已经写入文件")

    def load_cookie(self, username):  # 加载session
        with open("cookie_" + username + ".txt", 'rb') as f:
            s = pickle.load(f)
        return s


    def getListData(self, row, username, password, status, beginTime, endTime):
        '''表单查询'''
        log.info("-----表单查询接口调用开始-----")
        cookie = self.get_user_cookies(username, password)
        log.info("cookie：%s" % cookie)

        # self.get_session(username, password)
        path = self.get_exl_url(row)
        url = self.ip + path + "&?session_id=" + cookie
        log.info("接口地址：%s" % url)

        data = {
            "sortOrder": "asc",
            "pageSize": "30",
            "pageNumber": "1",
            "page": "1",
            "rows": "30",
            "status": status,
            "beginTime": beginTime,
            "endTime": endTime,
            "category": "",
            "level": "",
            "triggerCondition": ""
        }
        resobj = self.s.post(url=url , headers=self.header2, data=data)
        # resobj = s.post(url=url, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        if response == {'err': '', 'data': {'total': 0, 'rows': []}, 'ok': 'success'}:
            if os.path.exists('cookie_' + username + '.txt'):
                os.remove('cookie_' + username + '.txt')
                cookie = self.get_user_cookies(username, password)
                resobj = self.s.post(url=url + "&?session_id=" + cookie, headers=self.header2, data=data)
                code = resobj.status_code
                response = resobj.json()
        log.info("-----表单查询接口调用结束-----")
        return code, response


    def startFlowWithForm(self, row, username, password, formdata, processDefKey="zjg-hecha",
                          eventType="check", operator="", assignee="", sourceId=""):
        '''表单发起--填写核查表单'''
        log.info("-----填写核查表单接口调用开始-----")
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        formdata1 = json.dumps(formdata)
        data = {
            "operator": operator,
            "assignee": assignee,
            "sourceId": sourceId,
            "processDefKey": processDefKey,
            "eventType": eventType,
            "formdata": formdata1

        }
        resobj = self.s.post(url=url, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        log.info("-----填写核查表单接口调用结束-----")
        return code, response

    def disposeJGEventsForMerge(self, row, username, password, JGKpiCode, batchId, beginTime, endTime,
                                type="processStart", source="merge"):
        '''表单发起--提交核查申请'''
        log.info("-----提交核查申请接口调用开始-----")
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        data = {
            "type": type,
            "source": source,
            "JGKpiCode": JGKpiCode,
            "batchId": batchId,
            "beginTime": beginTime,
            "endTime": endTime
        }
        resobj = self.s.post(url=url, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        log.info("-----提交核查申请接口调用结束-----")
        return code, response


    def getItems(self, row, username, password, type):
        '''获取事项列表headers=self.header2,'''
        log.info("-----获取事项列表接口调用开始-----")
        cookie = self.get_user_cookies(username, password)
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        data = {
            "type": type,
            "sortOrder": "asc",
            "rows": 50,
            "processLabel": "process_num",
            "pageSize": 50,
            "pageNumber": 1,
            "page": 1
        }
        resobj = self.s.post(url=url + "?session_id=" + cookie, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        if response == {'err': '', 'data': {'total': 0, 'rows': []}, 'ok': 'success'}:
            if os.path.exists('cookie_' + username + '.txt'):
                os.remove('cookie_' + username + '.txt')
                cookie = self.get_user_cookies(username, password)
                resobj = self.s.post(url=url + "?session_id=" + cookie, headers=self.header2, data=data)
                code = resobj.status_code
                response = resobj.json()
        log.info("-----获取事项列表接口调用结束-----")
        return code, response

    def queryFormData(self, row, processInsId):
        '''获取事项相关'''
        log.info("-----流程审批处理接口调用开始-----")
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        data = {
            "processInsId": processInsId,

        }
        resobj = self.s.post(url=url, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        log.info("-----获取事项列表接口调用结束-----")
        return code, response

    def completeTaskWithForm(self, row, username, password, taskId, formdata, opionin):
        '''流程审批处理'''
        log.info("-----流程审批处理接口调用开始-----")
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        formdata1 = json.dumps(formdata)
        data = {
            "taskId": taskId,
            "opionin": opionin,
            "formdata": formdata1,
            "agree": "1"
        }
        resobj = self.s.post(url=url, headers=self.header2, data=data)
        code = resobj.status_code
        response = resobj.json()
        if response == {'err': '当前登录账号无权限处理此任务', 'errorcode': '1'}:
            if os.path.exists('cookie_' + username + '.txt'):
                os.remove('cookie_' + username + '.txt')
                cookie = self.get_user_cookies(username, password)
                url = self.ip + path
                resobj = self.s.post(url=url + "?session_id=" + cookie, headers=self.header2, data=data)
                code = resobj.status_code
                response = resobj.json()
        log.info("-----流程审批处理接口调用结束-----")
        return code, response


    def uploadFile(self, row, username, password):
        '''文件上传'''
        log.info("-----文件上传接口调用开始-----")
        # self.get_session(username, password)
        path = self.get_exl_url(row)
        url = self.ip + path
        log.info("接口地址：%s" % url)

        files = {
            "dir": (None, ''),
            "name": (None, ''),
            "file": (
            'fileupload.xls', open(os.path.join(fileupdown, 'fileupload.xls'), 'rb'), 'application/vnd.ms-excel')

        }
        resobj = self.s.post(url=url, files=files)
        # resobj = s.post(url=url, files=files)
        code = resobj.status_code
        response = resobj.json()
        log.info("-----文件上传接口调用结束-----")
        return code, response




if __name__ == "__main__":
    '''单元测试connect_kingbase'''
    files = {
        "dir": (None, ''),
        "name": (None, ''),
        "file": ('fileupload.xls', open(os.path.join(fileupdown, 'fileupload.xls'), 'rb'), 'application/vnd.ms-excel')

    }