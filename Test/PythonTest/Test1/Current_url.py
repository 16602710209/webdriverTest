# 导包
from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 通过超链接打开新闻界面
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
url = driver.current_url
time.sleep(2)
if url == "http://new.baidu.com":
    print("网址正确")
else:
    print("网址错误")
# 关闭浏览器
driver.quit()
