import time

import pyautogui

from common.globalmanager import get_pic_info
from common.guibase import GuiBase

getpic = get_pic_info()
gui = GuiBase()

class TestQQTalk():
    def test_qqlogin(self, user, pwd):
        """QQ登录"""
        pyautogui.hotkey('win', 'm')
        time.sleep(3)
        gui.click_picture(getpic['qq_icon_0625'], clicks=2, button='left')
        time.sleep(5)
        gui.rel_picture_click(getpic['qq_user_0625'], rel_x=-75, clicks=1, button='left')
        time.sleep(2)
        gui.type(user)
        time.sleep(5)
        gui.rel_picture_click(getpic['qq_pwd_0625'], rel_x=-75, clicks=2, button='left')
        time.sleep(2)
        gui.type(pwd)
        time.sleep(2)
        gui.click_picture(getpic['qq_login_0625'])
        gui.hotkey('CTRL', 'ALT', 'Z')
        time.sleep(2)
        assert gui.ispicture(getpic['qq_touxiang_0625'])

    def test_qqtalk(self, screenname):
        """QQ聊天"""
        time.sleep(3)
        #gui.click_picture(getpic['qq_login_ok_0625'], clicks=1, button='left')
        gui.rel_picture_click(getpic['qq_sousuo_0625'], rel_x=100, clicks=1, button='left')
        time.sleep(2)
        gui.input_cn(screenname)
        time.sleep(2)
        gui.hotkey('ENTER')
        time.sleep(2)
        gui.rel_picture_click(getpic['qq_biaoqing_0625'], rel_y=50, clicks=1, button='left')

    def test_qqsend(self, sendtext):
        gui.input_cn(sendtext)
        time.sleep(2)
        gui.hotkey('ENTER')


