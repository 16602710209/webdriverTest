# 导包
from selenium import webdriver
import time
import xlrd
from selenium.webdriver.common.keys import Keys
import os


# 封装
def qqEmail(filename):
    fileN = os.path.dirname(__file__) + r"/" + filename
    # 读取excel文件
    data = xlrd.open_workbook(fileN)
    # 读取excel文件中的第一个sheet中的表格
    table = data.sheets()[0]
    #  获取表格中的行数
    nrow = table.nrows

    for i in range(nrow):
        # 创建浏览器对象，并打开qq邮箱的网页
        driver = webdriver.Chrome()
        driver.get("http://email.qq.com")

        # 窗口最大化
        driver.maximize_window()

        # 点击”基本版“链接
        driver.find_element_by_link_text('基本版').click()
        # 输入账号
        driver.find_element_by_xpath('//*[@id="u"]').send_keys(table.row_values(i)[0])
        time.sleep(1)
        # 全选账号
        driver.find_element_by_xpath('//*[@id="u"]').send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        # 剪切账号
        driver.find_element_by_xpath('//*[@id="u"]').send_keys(Keys.CONTROL, 'x')
        time.sleep(1)
        # 粘贴账号
        driver.find_element_by_xpath('//*[@id="u"]').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        # 输入密码
        driver.find_element_by_xpath('//*[@id="p"]').send_keys(table.row_values(i)[1])
        time.sleep(1)
        # 全选密码
        driver.find_element_by_xpath('//*[@id="p"]').send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        # 剪切密码
        driver.find_element_by_xpath('//*[@id="p"]').send_keys(Keys.CONTROL, 'x')
        time.sleep(1)
        # 粘贴密码
        driver.find_element_by_xpath('//*[@id="p"]').send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        driver.quit()


if __name__ == '__main__':
    qqEmail("qq_data.xls")
