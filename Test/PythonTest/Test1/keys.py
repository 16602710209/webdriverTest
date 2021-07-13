'''

键盘事件案例 ：
1、百度seleniumm
2、删除多输入的m
3、再输入“空格 教程”
4、ctrl+a 全选文本框的内容
5、ctrl+x 剪切选择的内容
6、ctrl+v 粘贴复制的内容
7、回车代替单击，完成搜索
8、退出浏览器

'''

# 导包
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 1、百度seleniumm
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(2)

# 2、删除多输入的m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 3、再输入“空格 教程”
driver.find_element_by_id("kw").send_keys(" 教程")
time.sleep(2)

# 4、ctrl+a 全选文本框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)

# 5、ctrl+x 剪切选择的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)

# 6、ctrl+v 粘贴复制的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(2)

# 7、回车代替单击，完成搜索
driver.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(2)

# 8、退出浏览器
driver.quit()
