# 导包
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os

# 利用时间戳来定义文件名称
filename = time.strftime("%Y-%m-%d-%H-%M-%S")+".html"
# 获取当前所在路径
path = os.path.dirname(__file__)+r"/"
# 拼接文档名
filename = path + filename
print(filename)
# 获取需要运行的测试用例
discover = unittest.defaultTestLoader.discover(r"./", pattern="myMathTest*.py")
# 打开接收测试结果的html文件
with open(filename, "wb") as f:
    runner = HTMLTestRunner(f, verbosity=2, title="单元测试报告", description="第一次运行的结果")
    runner.run(discover)