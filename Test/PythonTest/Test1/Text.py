# 导包
from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获取文本
wenben = driver.find_element_by_xpath("//*[@id='s-hotsearch-wrapper']/div/a[1]/div").text
time.sleep(2)
print(wenben)
# 关闭浏览器
driver.quit()
