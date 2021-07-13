"""
1、打开淘宝网
2、点击天猫，进入天猫页面
3、选择女装，进入女装页面
4、返回到聚划算页面
"""

# 导包
from selenium import webdriver
import time

# 创建浏览器对象，获取淘宝首页
driver = webdriver.Chrome()
driver.get("https://www.taobao.com")
time.sleep(2)

# 点击天猫，进入天猫页面
driver.find_element_by_link_text("天猫").click()
time.sleep(2)

# 第一步：获取所有打开窗口的句柄
handlers = driver.window_handles
# 第二步：将聚划算的句柄绑定给driver
driver.switch_to.window(handlers[1])
# 选择女装，进入女装页面
driver.find_element_by_link_text("女装").click()
time.sleep(2)

# 返回天猫首页
driver.back()
time.sleep(2)


# 关闭浏览器对象
driver.close()