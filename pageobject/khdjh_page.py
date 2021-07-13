#!/usr/bin/python
# -*- coding:utf-8 -*-

from common.guibase import GuiBase
from common.webbase import WebBase
import time
import pyautogui
from selenium import webdriver
from common.logger import Logger
from common.globalmanager import get_pic_info


runclient = (1725, 1060)
hostip = "10.11.1.171"
benjiip = "10.11.124.50"
benjimac = "1C-69-7A-28-85-7E"


log = Logger('khdjh_page.py').getLogger()
picInfo = get_pic_info()

class KHDJHPage():
    def __init__(self):
        self.runclient = runclient
        self.hostip = hostip
        self.benjiip = benjiip
        self.benjimac = benjimac
        self.username = "admin"
        self.psw = "123ABCdef*"


        self.Test = GuiBase()
        self.url = "http://" + self.hostip + ":8888/core/login?sys_code=itx&single_mode=itx&login_style=single_sys_info&sys_name=%E5%9F%BA%E7%A1%80%E5%B9%B3%E5%8F%B0&user=&tab_name_show="
        '''WEB端页面元素'''
        #基础平台登录相关
        self.loc_user = ("id","username")
        self.loc_psw = ("id","password")
        self.loc_login = ("xpath",".//div[@class='btn-content']/a[@class='btn-login']")
        #添加主机相关
        self.loc_hostgl = ("xpath", ".//ul[@class='navigation']/li[2]/a/div/span[text()='主机管理']")
        self.loc_hostlist = ("xpath",".//ul[@id='itx.host']/li/a/div/span[text()='主机列表  ']")
        self.loc_addhost = ("xpath",".//div[@id='options']/a[1]/span/span[text()='添加主机']")
        self.loc_danji = ("xpath",".//table[@class='table_form']/tbody/tr[2]/td[2]/input[@id='r-1']")
        self.loc_lianwang = ("xpath",".//table[@class='table_form']/tbody/tr[2]/td[2]/input[@id='r-2']")
        self.loc_hostname = ("xpath",".//table[@class='table_form']/tbody/tr[3]/td[2]/input[2]")
        self.loc_hostcode = ("xpath",".//table[@class='table_form']/tbody/tr[3]/td[4]/input")
        self.loc_seleuser = ("xpath",".//table[@class='table_form']/tbody/tr[4]/td[2]/a/span/span[text()='选择用户']")
        self.loc_hostuser = ("id","name")
        self.loc_hostsele = ("xpath",".//form[@id='user_search']/div/a/span/span[text()='查询']")
        self.loc_hostfirstuser = ("xpath",".//tr[@id='datagrid-row-r2-2-0']/td[1]/div/input")
        self.loc_ok = ("xpath",".//div[@class='dialog-button']/a/span/span[text()='确 定']")
        self.loc_hostIP = ("xpath",".//table[@class='table_form']/tbody/tr[5]/td[2]/input")
        self.loc_hostMac = ("xpath",".//table[@class='table_form']/tbody/tr[5]/td[4]/input")
        self.loc_hosthadenum = ("xpath",".//table[@class='table_form']/tbody/tr[6]/td[2]/input")
        self.loc_hostseleleve = ("xpath",".//table[@class='table_form']/tbody/tr[7]/td[2]/a/span/span[text()='选择密级']")
        self.loc_hostleve1 = ("xpath",".//tr[@id='datagrid-row-r3-2-0']/td[1]/div/input")
        self.loc_hostleve2 = ("xpath",".//tr[@id='datagrid-row-r3-2-1']/td[1]/div/input")
        self.loc_hostleve3 = ("xpath",".//tr[@id='datagrid-row-r3-2-2']/td[1]/div/input")

        self.loc_homenum = ("xpath",".//table[@class='table_form']/tbody/tr[8]/td[2]/input")
        self.loc_beizhu = ("id","textarea")
        self.loc_save = ("xpath",".//div[@class='dialog-button']/a[1]/span/span[text()='保 存']")
        self.loc_getazcode = ("xpath",".//tr[@id='datagrid-row-r1-2-0']/td[2]/div")
        #主机查询相关
        self.loc_stat = ("xpath",".//form[@id='host_search']/div/span[2]/span/span")
        self.loc_select = ("xpath",".//form[@id='host_search']/div/a[1]/span/span[text()='查询']")
        self.loc_outcode = ("xpath",".//tr[@id='datagrid-row-r1-2-0']/td[9]/div")
        self.loc_normal = ("xpath",".//div[@class='panel combo-p']/div/div[text()='正常']")
        self.loc_hostcancel = ("xpath",".//ul[@id='itx.host']/li[2]/a/div/span[text()='注销主机列表  ']")
        self.loc_hostusername = ("xpath",".//tr[@id='datagrid-row-r1-2-0']/td[5]/div")




    def Client_act(self,acttype,IP,HOST,USER,isok=None,azcode=None):
        '''终端激活，选择联网激活--联网手动激活，填写服务器ip，通讯服务器端口（默认15001），点击下一步选择部门、用户、输入备注等信息，点击激活'''
        log.info("-----终端激活开始-----")
        self.Test.click_picture(picInfo["khdjh"]["netAct"])
        log.info("点击下一步")
        self.Test.click_picture(picInfo["khdjh"]["next"])
        if acttype == "1":
            log.info("点击联网手动激活")
            self.Test.click_picture(picInfo["khdjh"]["netHandAct"])
            log.info("输入服务器IP")
            self.Test.rel_picture_click(picInfo["khdjh"]["inputIP"], rel_y=30,clicks=3)
            pyautogui.press("delete")
            pyautogui.typewrite(IP)  # 输入
            log.info("输入host")
            self.Test.rel_picture_click(picInfo["khdjh"]["inputHost"], rel_y=30,clicks=3)
            pyautogui.press("delete")
            pyautogui.typewrite(HOST)  # 输入
            log.info("点击下一步")
            self.Test.click_picture(picInfo["khdjh"]["next"])
            log.info("选择所属部门")
            self.Test.rel_picture_click(picInfo["khdjh"]["department"], rel_x=110)
            self.Test.mouse_click(posy=-50, flag=2)
            self.Test.click_picture(picInfo["khdjh"]["queding"])

            log.info("选择用户")
            self.Test.rel_picture_click(picInfo["khdjh"]["user"], rel_x=110)
            self.Test.input_cn(USER)  # 输入
            log.info("选择密级")
            self.Test.rel_picture_click(picInfo["khdjh"]["level"], rel_x=110)
            self.Test.mouse_click(posy=50, flag=2)
        elif acttype == "2":
            log.info("点击联网自动激活")
            self.Test.click_picture(picInfo["khdjh"]["netAutoAct"])
            self.Test.rel_picture_click(picInfo["khdjh"]["setNum"], rel_x=110,clicks=3)
            pyautogui.typewrite(azcode)  # 输入
            log.info("输入服务器IP")
            self.Test.rel_picture_click(picInfo["khdjh"]["inputIP"], rel_y=30,clicks=3)
            pyautogui.press("delete")
            pyautogui.typewrite(IP)  # 输入
            log.info("输入host")
            self.Test.rel_picture_click(picInfo["khdjh"]["inputHost"], rel_y=30)
            pyautogui.press("delete")
            pyautogui.typewrite(HOST)  # 输入
        log.info("点击下一步")
        self.Test.click_picture(picInfo["khdjh"]["next"])
        pyautogui.moveRel(0, -50, duration=0.25)
        if isok == None:
            self.Test.click_picture(picInfo["khdjh"]["queding"])
        elif isok == "1":
            print("不需确定")
        log.info("点击提交")
        self.Test.click_picture(picInfo["khdjh"]["submit"])
        log.info("-----终端激活结束-----")



    def Client_Asser(self,asser):
        '''判断是否激活'''
        log.info("-----判断是否激活开始-----")
        # p5 = Test.get_picture("runclient1.png")
        # self.Test.mouseClick(p5)
        pyautogui.click(*self.runclient,1,self.Test.duration, button='right')
        self.Test.click_picture(picInfo["khdjh"]["showwindow"])

        if asser == "1":
            '''激活成功断言'''
            result = self.Test.ispicture(picInfo["khdjh"]["yesAct"])
            self.Test.click_picture(picInfo["khdjh"]["outclient"])
            log.info("-----判断激活成功结束-----")
            return result
        elif asser == "0":
            '''未激活断言'''
            result = self.Test.ispicture(picInfo["khdjh"]["noAct"])
            self.Test.click_picture(picInfo["khdjh"]["outclient"])
            log.info("-----判断未激活结束-----")
            return result



    def client_cancel(self,cancel_code):
        '''后置条件：客户端注销'''
        log.info("-----注销客户端开始-----")
        pyautogui.click(*self.runclient,1,self.Test.duration, button='right')
        self.Test.click_picture(picInfo["khdjh"]["client_cancel"])
        pyautogui.typewrite(cancel_code)  #
        self.Test.click_picture(picInfo["khdjh"]["queding"])
        self.Test.click_picture(picInfo["khdjh"]["queren"])
        self.Test.click_picture(picInfo["khdjh"]["queding"])
        log.info("-----注销客户端结束-----")


    def Client_open(self):
        '''点击终端激活向导'''
        log.info("-----点击终端激活向导开始-----")
        self.Test = GuiBase()
        time.sleep(1)
        self.Test.click_picture(picInfo["khdjh"]["client_activation"])
        log.info("-----点击终端激活向导结束-----")



    def ClientDan_act(self,acttype,USER,orgType=None,orgName=None):
        log.info("-----终端单机激活开始-----")
        log.info("点击单机激活")
        self.Test.click_picture(picInfo["khdjh"]["danAct"])
        log.info("点击下一步")
        self.Test.click_picture(picInfo["khdjh"]["next"])
        #选择激活方式
        if acttype == "1":
            log.info("点击有管理中心激活")
            self.Test.click_picture(picInfo["khdjh"]["HaveCenter"])
            log.info("点击下一步")
            self.Test.click_picture(picInfo["khdjh"]["next"])
            self.Test.click_picture(picInfo["khdjh"]["okshi"])
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")
            self.Test.click_picture(picInfo["khdjh"]["queding"])
            #填写激活信息
            log.info("选择所属部门")
            self.Test.rel_picture_click(picInfo["khdjh"]["department"], rel_x=110)
            self.Test.moveto(posy=-50,flag=2)
            self.Test.click_picture(picInfo["khdjh"]["queding"])
            log.info("选择用户")
            self.Test.rel_picture_click(picInfo["khdjh"]["user"], rel_x=110)
            self.Test.input_cn(USER)  # 输入
            log.info("选择密级")
            self.Test.rel_picture_click(picInfo["khdjh"]["level"], rel_x=110)
            self.Test.mouse_click(posy=50,flag=2)
            self.Test.click_picture(picInfo["khdjh"]["next"])

        elif acttype == "2":
            log.info("点击无管理中心激活")
            self.Test.click_picture(picInfo["khdjh"]["NotCenter"])
            log.info("点击下一步")
            self.Test.click_picture(picInfo["khdjh"]["next"])
            self.ClientDan_neworg(orgType,orgName,USER)
            #填写激活信息
            log.info("选择所属部门")
            self.Test.rel_picture_click(picInfo["khdjh"]["department"], rel_x=110)
            self.Test.click_picture(picInfo["khdjh"]["deptAuto"])
            self.Test.click_picture(picInfo["khdjh"]["queding"])
            log.info("选择用户")
            self.Test.rel_picture_click(picInfo["khdjh"]["user"], rel_x=110)
            self.Test.input_cn(USER)  # 输入
            log.info("选择密级")
            self.Test.rel_picture_click(picInfo["khdjh"]["level"], rel_x=110)
            self.Test.mouse_click(posy=50,flag=2)

        self.Test.click_picture(picInfo["khdjh"]["next"])
        self.Test.click_picture(picInfo["khdjh"]["queding"])
        log.info("点击提交")
        self.Test.click_picture(picInfo["khdjh"]["submit"])
        log.info("-----终端单机激活结束-----")


    def ClientDan_login(self,username,psw):
        '''单机版账号登录'''
        log.info("-----单机版账号登录开始-----")
        #登录admin
        pyautogui.click(*self.runclient, 1,self.Test.duration, button='right')
        self.Test.click_picture(picInfo["khdjh"]['clientlogin'])
        pyautogui.typewrite(username)
        pyautogui.press("tab")
        pyautogui.typewrite(psw)
        self.Test.click_picture(picInfo["khdjh"]["loginbtn"])
        log.info("-----单机版账号登录结束-----")

    def ClientDan_out(self):
        '''退出登录'''
        log.info("-----退出登录开始-----")
        pyautogui.click(*self.runclient, 1,self.Test.duration, button='right')
        self.Test.click_picture(picInfo["khdjh"]["accountOut"])
        self.Test.click_picture(picInfo["khdjh"]["tuichu"])
        log.info("-----退出登录结束-----")

    def ClientDan_cancel(self):
        '''单机版注销'''
        log.info("-----单机版注销开始-----")
        #注销
        pyautogui.click(*self.runclient,1,self.Test.duration, button='right')
        self.Test.click_picture(picInfo["khdjh"]["showwindow"])
        self.Test.rel_picture_click(picInfo["khdjh"]["shouye"],rel_y=45)
        self.Test.click_picture(picInfo["khdjh"]["adminMana"])
        self.Test.click_picture(picInfo["khdjh"]["tercancel"])
        self.Test.click_picture(picInfo["khdjh"]["queren"])
        self.Test.click_picture(picInfo["khdjh"]["queding"])
        self.Test.click_picture(picInfo["khdjh"]["outclient"])
        log.info("-----单机版注销结束-----")


    def Client_run(self):
        '''运行托盘基础平台客户端程序'''
        log.info("-----运行托盘基础平台客户端程序开始-----")
        self.Test = GuiBase()
        time.sleep(1)
        pyautogui.click(*self.runclient, 2,self.Test.duration, button='right')
        log.info("-----运行托盘基础平台客户端程序结束-----")



    def act_hou(self):
        '''激活后置条件'''
        log.info("-----激活后置开始-----")
        pyautogui.click(*self.runclient, 1,self.Test.duration, button='right')
        self.Client_open()
        self.Test.click_picture(picInfo["khdjh"]["houZhi"])
        self.Test.click_picture(picInfo["khdjh"]["outclient2"])
        log.info("-----激活后置结束-----")



    def ClientDan_neworg(self,orgType,orgName,userName):
        '''组织机构创建'''
        log.info("-----组织机构创建开始-----")
        self.Test.click_picture(picInfo["khdjh"]["NewOrg"])
        self.Test.click_picture(picInfo["khdjh"]["AddOrg"])
        #选择类型
        if orgType == "1":
            self.Test.click_picture(picInfo["khdjh"]["Company"])

        elif orgType == "2":
            self.Test.click_picture(picInfo["khdjh"]["Deptmentadd"])
        #输入名称
        self.Test.rel_picture_click(picInfo["khdjh"]["orgName"], rel_x=110)
        self.Test.input_cn(orgName)  # 输入
        #保存
        self.Test.click_picture(picInfo["khdjh"]["Save"])
        #添加用户
        self.Test.rel_picture_click(picInfo["khdjh"]["orgstart"], rel_y=25)
        self.Test.click_picture(picInfo["khdjh"]["AddUser"])
        #输入用户名
        self.Test.rel_picture_click(picInfo["khdjh"]["UserName"], rel_x=110)
        self.Test.input_cn(userName)  # 输入
        self.Test.click_picture(picInfo["khdjh"]["Save"])
        self.Test.click_picture(picInfo["khdjh"]["queding"])
        log.info("-----组织机构创建结束-----")



    def ClientShowWindow(self):
        '''显示主窗口'''
        log.info("-----显示主窗口开始-----")
        pyautogui.click(*self.runclient, 1,self.Test.duration, button='right')
        Test = GuiBase()
        Test.click_picture(picInfo["khdjh"]["showwindow"])
        log.info("-----显示主窗口结束-----")













if __name__ == "__main__":
    Test = KHDJHPage()
    time.sleep(3)
    Test.ClientDan_neworg("2","自动化测试机构","自动化测试用户")

