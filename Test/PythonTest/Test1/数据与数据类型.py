#导包
from selenium import webdriver
#创建浏览器对象
driver = webdriver.Chrome()
#打开百度首页
driver.get('http://www.baidu.com')
#在百度文本框中输入selenium
driver.find_element_by_id("kw").send_keys("selenium")
#点击百度
driver.find_element_by_id("su").click()
#关闭浏览器
# driver.quit()
