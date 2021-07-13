# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 等待两秒 放大窗口
time.sleep(2)
driver.maximize_window()

# 控制鼠标悬浮到“设置”按钮上
setButton = driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
# 将对“设置”按钮的操作行为封装到ActionChains，到这一步，鼠标对象已经知道要干啥事了，还没开始动呢
ActionChains(driver).move_to_element(setButton).perform()
time.sleep(3)
#  在百度文本框中鼠标右键
webEdit = driver.find_element_by_id("kw")
ActionChains(driver).context_click(webEdit).perform()

time.sleep(3)
driver.close()