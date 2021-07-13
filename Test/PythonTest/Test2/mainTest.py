"""
这是一个主测试文件，不是用来写测试用例的，而是用来组织测试用例执行的
"""

# 导包
import unittest

# 将需要测试的用例放进加载器中
discover = unittest.defaultTestLoader.discover(r'./', pattern='myMathTest*.py')
# 打开一个文件用于写入测试用例运行的结果
with open(r"./res.txt", "w", encoding="utf-8") as f:
    # 将测试结果写入文件中
    runner = unittest.TextTestRunner(f, descriptions="用于测试math类的用例执行", verbosity=2)
    # 运行测试用例
    runner.run(discover)
