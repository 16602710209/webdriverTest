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
# 定义字典数据，用来存储注册数据的（用户名、密码、确认密码，email）
# 字典中存数据，字典当列表
from selenium import webdriver
import time
dictData = [{"username": "", "email": "nz1903_005@163.com", "password": "123456", "repassword": "123456", "expect": "请输入用户名"},
            {"username": "小青蛙1903_006", "email": "nz1903_006@163.com", "password": "123456", "repassword": "123456", "expect": "用户名不符合格式要求"},
            {"username": "小青蛙", "email": "nz1903_007@163.com", "password": "123456", "repassword": "123456", "expect": "用户名不符合格式要求"}]

for i in dictData:
    # 创建浏览器对象 进入网页
    driver = webdriver.Chrome()
    driver.get("http:47.105.47.131/verydows/")

    # 在表单中输入对应数据
    driver.find_element_by_link_text("免费注册").click()
    driver.find_element_by_id("username").send_keys(i["username"])
    driver.find_element_by_id("email").send_keys(i["email"])
    diver.find_element_by_id("password").send_keys(i["password"])
    driver.find_element_by_id("repassword").send_keys(i["repassword"])
    driver.find_element_by_link_text("立即注册").click()

    # 因为有一个中间页面的跳转，此处要强制等待一下，让他跳转过去
    time.sleep(5)
    # 断言
    expectValue = i["expect"]
    actuaValue = driver.find_element_by_xpath('//*[@id="register_form"]/div/dl[1]/dd/span/font').text()
    if expectValue == actuaValue:
        print("注册username反向测试用例通过")
    else:
        print("注册username反向测试用例失败")

    # 关闭浏览器对象
    driver.quit()
