import pyautogui

# 1.全图截屏，截全图并设置保存图片的位置和名称，并返回图片属性
pyautogui.screenshot(r'E:\Test\client_demo\01.png')

# 2.不截全图，截取区域图片，截取区域region参数为：左上角xy坐标值，宽度和高度
pyautogui.screenshot(r'E:\Test\client_demo\02.png', region=(0, 0, 200, 200))

# 3.获得文件图片再现在的屏幕上面的坐标，返回的是一个元组（top,left,width,height）,如果截图没有找到，函数返回None
a = pyautogui.locateOnScreen(r'E:\Test\client_demo\02.png')
print(a)

# 4.获得文件图片再现在的屏幕上面的中心坐标
x, y = pyautogui.center(a)
print(x, y)

# 5.这一步与上面四行代码作用一样，识别到图像返回图像中心点xy坐标，识别不到返回None
x, y = pyautogui.locateCenterOnScreen(r'E:\Test\client_demo\02.png')
print(x, y)

# 匹配屏幕所有与目标图片的对象，返回所有定位信息的元组
# 如，打印多个（left=0, top=0, width=300, height=400）
pyautogui.locateAllOnScreen(r'E:\Test\client_demo\02.png')
