"""
要求：百度文本框输入selenium，点击百度一下
    1.百度文本框
    2.百度一下
使用ID属性定位
    1.确定要操作的对象
    2.获取id属性（kw/su）
    3.其他操作
"""
#导包、创建浏览器对象、获取一下url地址
from selenium import webdriver
import time
#driver:就是一个普通的变量，dr也行
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#通过ID来定位文本框和百度一下
driver.find_element_by_id("kw").send_keys("英短")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
#退出浏览器对象
driver.quit()
