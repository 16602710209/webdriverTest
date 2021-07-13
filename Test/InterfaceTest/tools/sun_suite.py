"""
目标：
    1、搜索组装测试套件
    2、运行测试套件并生成套件
"""
# 导包unittest HTMLTestRunner time
import unittest
import time
from InterfaceTest.tools.HTMLTestRunner import HTMLTestRunner
# 第一步：组装测试套件
suite = unittest.defaultTestLoader.discover("./case", pattern="test*.py")
# 第二步：执行报告存放路径及文件名称
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 第三步：运行测试套件并生成测试报告
with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
