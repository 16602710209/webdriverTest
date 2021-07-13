# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 创建浏览器对象，进入百度网页
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#  最大化窗口
driver.maximize_window()

# 找到到“设置”链接
setting = driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
# 将鼠标悬浮在“设置”连接上这个动作封装在ActionChains中，并且开始执行
ActionChains(driver).move_to_element(setting).perform()
time.sleep(2)

# 打开搜索设置按钮
driver.find_element_by_xpath("//*[@id='s-user-setting-menu']/div/a[1]").click()
time.sleep(2)

# 点击保存设置
driver.find_element_by_xpath("//*[@id='se-setting-7']/a[2]").click()

# 弹出警告提示框
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
# 关闭driver对象
driver.quit
