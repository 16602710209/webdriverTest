# 导包
import unittest
from myMath import mymath

class myMathTest(unittest.TestCase):
    def setUp(self):
        self.mm = mymath()

    def test_add_1(self):
        actualValue = self.mm.jia(2, 3)
        expectValue = 5
        # 断言
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_add_2(self):
        actualValue = self.mm.jia("abc", "def")
        expectValue = "abcdef"
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_add_3(self):
        actualValue = self.mm.jia("abc", 123)
        expectValue = "abc123"
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")


    def tearDown(self):
        pass

if __name__=="__main__":
    # 直接使用discover
    discover = unittest.defaultTestLoader.discover(r"./", pattern="myMathTest.py")
    # 使用runner运行器测试集
    with open("./re.txt", "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(f, descriptions="用于测试math类的用例执行", verbosity=2)
        runner.run(discover)