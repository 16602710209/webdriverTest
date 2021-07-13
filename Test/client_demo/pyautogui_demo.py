'''
基于图像识别的客户端Ui自动化
模拟人工操作QQ登录
'''

import pyautogui
import time

#模拟快捷键，win+m 回到桌面
pyautogui.hotkey('win','m')

#需要等几秒页面反应
time.sleep(2)

#模拟鼠标左键双击击，双击qq图标
#（1）图像定位到新建按钮，并点击
box = pyautogui.locateOnScreen(r'C:\Users\19344\Desktop\client_demo\qq_icon.png')
print(box)
#（2）获取定位到的图片的中心点坐标
x,y = pyautogui.center(box)
print(x,y)
#（3）移动到中心点坐标双击
pyautogui.click(x,y,clicks=2,button='left')

#需要等几秒页面反应
time.sleep(3)

#定位到输入密码框，点击选中，输入用户名
#（1）定位到输入密码框旁边的箭头（我们要选择定位的图片最好是不可变化的）
box = pyautogui.locateOnScreen(r'C:\Users\19344\Desktop\client_demo\qq_user.png')
print(box)
#（2）获取定位到的图片的中心点坐标
x,y = pyautogui.center(box)
print(x,y)
#（3）移动到中心点坐标双击
pyautogui.moveTo(x,y)
#（4）相对位置向左移动一段距离
pyautogui.moveRel(-100,0)
#（5）在移动后的位置左击一下，选择输入框
pyautogui.click()
#（6）输入用户名
pyautogui.typewrite('2596873309',interval=0.2)

#定位到输入密码框，点击选中，输入密码
#（1）定位到输入密码框旁边的箭头（我们要选择定位的图片最好是不可变化的）
box = pyautogui.locateOnScreen(r'C:\Users\19344\Desktop\client_demo\qq_psw.png',minSearchTime=10)
print(box)
#（2）获取定位到的图片的中心点坐标
x,y = pyautogui.center(box)
print(x,y)
#（3）移动到中心点坐标双击
pyautogui.moveTo(x,y)
#（4）相对位置向左移动一段距离
pyautogui.moveRel(-100,0)
#（5）在移动后的位置左击一下，选择输入框
pyautogui.click()
#（6）输入密码
pyautogui.typewrite('lcy12345678',interval=0.2)

#定位到登录按钮，鼠标左键点击一次
#（1）定位到输入密码框旁边的箭头（我们要选择定位的图片最好是不可变化的）
box = pyautogui.locateOnScreen(r'C:\Users\19344\Desktop\client_demo\qq_login.png',minSearchTime=10)
print(box)
#（2）获取定位到的图片的中心点坐标
x,y = pyautogui.center(box)
print(x,y)
#（3）点击中心点坐标
pyautogui.click(x,y)









