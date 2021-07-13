#导包、创建浏览器对象、获取一下url地址
from selenium import webdriver
import time
#driver:就是一个普通的变量，dr也行
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#通过name来定位文本框和百度一下
driver.find_element_by_name("wd").send_keys("布偶猫")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
#关闭浏览器
driver.quit()