# 导包
from selenium import webdriver
import time

# 1、创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.qq.com")

#  2、最大化窗口、点击邮箱图标
driver.maximize_window()
driver.find_element_by_link_text("Qmail").click()
time.sleep(2)

# 3、跳转到邮箱登录界面（窗口），涉及到多窗口的处理，拿句柄
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 4、现在先验证窗口是都跳转成功
driver.find_element_by_link_text("基本版").click()
time.sleep(2)

# 5、拿到新页面的句柄
# handles1 = driver.window_handles
# driver.swith_to.window(handles1[1])

# 6、输入帐号和密码,点击登录
driver.find_element_by_id("u").send_keys("2490158860")
time.sleep(2)
driver.find_element_by_id("p").send_keys("w19950716j..")
time.sleep(2)
driver.find_element_by_id("go").click()
time.sleep(2)
# 关闭浏览器
driver.quit()