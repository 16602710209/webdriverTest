#导包
from selenium import webdriver
import time
#创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#css的类选择器定位百度文本框，使用css的id选择器定位百度一下按钮
driver.find_element_by_css_selector(".s_ipt").send_keys("美短加白")
time.sleep(2)
driver.find_element_by_css_selector("#su").click()
time.sleep(2)
#关闭浏览器
driver.quit()