import pytest
import time
from common.guibase import GuiBase
from common.globalmanager import get_pic_info
import pyautogui


gui = GuiBase()
picInfo = get_pic_info()

class TestCase():
    def test_QQ_001(self):
        """用例一：QQ登录"""
        pyautogui.hotkey('win', 'm')
        time.sleep(3)
        gui.click_picture(picInfo['qq_icon'], clicks=2, button='left')
        gui.rel_picture_click(picInfo['qq_user'], rel_x=-100, clicks=1, button='left')
        gui.type('346639189')
        gui.rel_picture_click(picInfo['qq_pwd'], rel_x=-100, clicks=1, button='left')
        gui.type('qqmima123')
        gui.click_picture(picInfo['qq_login'])
        assert gui.ispicture(picInfo['login_ok'])


tc = TestCase()
tc.test_QQ_001()

