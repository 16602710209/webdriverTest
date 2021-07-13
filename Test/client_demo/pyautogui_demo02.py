import pyautogui


# 开始很慢，不断加速
pyautogui.moveTo(100, 200, 2, pyautogui.easeInQuad)

# 开始很快，不断减速
pyautogui.moveTo(200, 300, 2, pyautogui.easeOutQuad)

# 开始和结束都快，中间比较慢
pyautogui.moveTo(300, 400, 2, pyautogui.easeInOutQuad)

# 一步一步徘徊前进
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)

# 徘徊幅度更大，甚至超过起点和终点
pyautogui.moveTo(50, 50, 2, pyautogui.easeInElastic)

