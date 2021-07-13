"""
需求：使用数据驱动的模型，编写电商系统正向用例的脚本
1、打开verydos系统首页
2、点击“免费注册”按钮
3、输入有效用户名，（xxx）
4、输入有效邮箱，输入有效密码
5、输入有效确认密码
6、已阅读按钮
7、点击“同意协议，立即注册”

"""
# 导包
import xlrd
from selenium import webdriver
import time

# 打开excel文件
data = xlrd.open_workbook(r"./qq_data.xls")
# 获取索引为0的一个sheet页，也就是sheet1
table = data.sheets()[0]
# 获取sheet页中指定的行数据和列数据
nrow = table.nrows
ncol = table.ncols
# 循环每一行的数据
for i in range(nrow):
    print(table.row_values(i)[0])
    print(table.row_values(i)[1])
    print(nrow)
    print(ncol)

    # 创建浏览器对象,并打开qq邮箱登录页面
    driver = webdriver.Chrome()
    driver.get("https://mail.qq.com/")

    driver.find_element_by_xpath('/html/body/div/div[1]/div/a[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="u"]').send_keys(table.row_values(i)[0])
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="p"]').send_keys(table.row_values(i)[1])
    time.sleep(3)
    driver.quit()

