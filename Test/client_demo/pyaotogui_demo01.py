import pyautogui


# 1、模拟鼠标操作
# 显示鼠标当前的坐标值
x, y = pyautogui.position()
print(x, y)

# 将鼠标以0.25每秒的速度移动到（500，500）的坐标位置上
pyautogui.moveTo(500, 500, duration=0.25)

# 将鼠标以0.25每秒的速度向左移动100像素的距离
pyautogui.moveRel(-100, 0, duration=0.25)

# 按住鼠标左键，以每秒0.25的速度拖拽到（100，200）的坐标位置上
pyautogui.dragTo(100, 200, duration=0.25, button="left")

# 按住鼠标左键，以每秒0.25的速度向上拖拽60像素的距离
pyautogui.dragRel(0, -60, duration=0.25, button="left")

# 鼠标点击，点击（100，200）位置，clicks点击次数，interval点击间隔时间0.1s，button左键
pyautogui.click(x=100, y=200, clicks=2, interval=0.1, button="left")

# 鼠标双击，鼠标在（100，150），位置左击两下
pyautogui.doubleClick(x=100, y=150, button="left")

# 鼠标三击，如果不传参就是当前位置点击
pyautogui.tripleClick()

# 获取当前鼠标的x, y的坐标
x, y = pyautogui.position()
print(x, y)

# # 鼠标左键按下再松开，如果不传参数，就是当前位置按下松开
pyautogui.mouseDown(button="right", x=100, y=200)  # 移动到（100，200）位置，按下鼠标右键
pyautogui.mouseUp(button="right", x=100, y=200)  # 移动到（100，200）位置，松开鼠标右键

# 鼠标滚动，移动到（100，100）位置再向上滚动300格（负数是向下）
pyautogui.scroll(300, x=500, y=600)
