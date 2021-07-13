# 导包
from selenium import webdriver
import time

# 加载浏览器
driver = webdriver.Chrome(executable_path=r'E:\Test\web_demo\chromedriver.exe')
# 进入QQ邮箱登录界面
driver.get('https://mail.qq.com/')

# 窗口最大化
driver.maximize_window()

# 等待加载时间
time.sleep(2)

# 切换到ifram里
el_ifram = driver.find_element_by_id('login_frame')
driver.switch_to.frame(el_ifram)

# 定位并输入用户名
el_user = driver.find_element_by_id('u')
el_user.send_keys('346639189')

# 定位并输入密码
el_password = driver.find_element_by_id('p')
el_password.send_keys('qqmima123')

# 点击登录
el_login = driver.find_element_by_id('login_button')
el_login.click()

# 关闭浏览器
driver.quit()
