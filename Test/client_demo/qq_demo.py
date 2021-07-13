# 导包
import pyautogui
import time

# 回到桌面
pyautogui.hotkey('win', 'm')

# 等待时间
time.sleep(3)

# 识别QQ位置,并且左键双击
x, y =pyautogui.locateCenterOnScreen(r'E:\Test\client_demo\qq_icon.png')
pyautogui.doubleClick(x, y, button='left')

# 等待时间
time.sleep(3)

# 识别qq号位置
x, y = pyautogui.locateCenterOnScreen(r'E:\Test\client_demo\qq_user.png')
# 将鼠标移动到中心坐标位置
pyautogui.moveTo(x, y, duration=0.25)
# 将鼠标的位置向左平移100个像素距离
pyautogui.moveRel(-100, 0, duration=0.25)
# 在移动后的位置点击一下，选择输入框
pyautogui.click()
# 输入QQ账号
pyautogui.typewrite('346639189', interval=0.25)

# 识别QQ密码位置
x, y = pyautogui.locateCenterOnScreen(r'E:\Test\client_demo\qq_password.png')
# 将鼠标的位置移动到中心坐标位置
pyautogui.moveTo(x, y, duration=0.25)
# 将鼠标向左平移100个像素的距离
pyautogui.moveRel(-100, 0, duration=0.25)
# 在移动后的位置点击一下，选择输入框
pyautogui.click()
# 输入qq密码
pyautogui.typewrite('qqmima123', interval=0.3)

# # 识别登录位置

# # x, y = pyautogui.locateCenterOnScreen(r'E:\Test\client_demo\qq_login.png', minSearchTime=10)
# # # 双击x,y的位置登录
# # pyautogui.click(x, y)

# 将鼠标下移75个像素
pyautogui.moveRel(0, 75, duration=0.25)
pyautogui.click()


