#导包
from selenium import webdriver
import time
#创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#通过超链接打开新闻界面
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
titleText=driver.title
time.sleep(2)
print(titleText)
if titleText == "百度新闻——海量中文资讯平台":
    print("标题正确")
else :
    print("标题错误")
#关闭浏览器
driver.quit()