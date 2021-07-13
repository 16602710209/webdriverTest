# 导包
from selenium import webdriver
import csv
import time
from selenium.webdriver.common.keys import Keys

# 获取文件
with open(r"qq_data_csv.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)

    # 遍历文件
    for i in data:

        # 创建浏览器对象，并打开网址
        driver = webdriver.Chrome()
        driver.get("https://mail.qq.com/")

        # 点击”基础版“链接
        driver.find_element_by_link_text("基本版").click()
        # 找到账号文本框，先将文本框内已有的账号删除，再输入对应的账号
        # driver.find_element_by_xpath('//*[@id="u"]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('//*[@id="u"]').send_keys(i[0])
        time.sleep(3)

        # 找到密码文本框，先将文本框内已有的账号删除，再输入对应的密码
        # driver.find_element_by_xpath('//*[@id="p"]').send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath('//*[@id="p"]').send_keys(i[1])
        time.sleep(3)

        driver.quit()