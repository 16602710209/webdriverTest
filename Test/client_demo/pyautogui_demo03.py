import pyautogui


# 键盘输入英文字符，每次输入间隔0.25秒，输入Hello World!
pyautogui.typewrite('Hello,World!', interval=0.25)

# 键盘按下并松开按键，按下并松开（轻敲）回车键
pyautogui.press('enter')

# 按键按下，按下’shift‘键
pyautogui.keyDown('shift')

# 按键松开，松开'shift'
pyautogui.keyUp('shift')

# 键盘组合键，组合按键（win+m）,回到桌面功能，按下并松开win和m键
pyautogui.hotkey('win', 'm')
