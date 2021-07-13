from selenium import webdriver
import time


# 1.浏览器相关操作
driver = webdriver.Chrome(executable_path=r'E:\Test\web_demo\chromedriver.exe')

time.sleep(1)

# 浏览器最大化
driver.maximize_window()

# 获取浏览器的尺寸
a = driver.get_window_size()
print(a)

# 获取浏览器所在位置的坐标
b = driver.get_window_position()
print(b)

time.sleep(2)

# 关闭当前页面
driver.close()

# 关闭全部页面
driver.quit()
