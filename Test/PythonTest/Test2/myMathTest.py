# 导包
import unittest
from myMath import mymath

class myMathTest(unittest.TestCase):
    def setUp(self):
        self.mm = mymath()

    def test_add_1(self):
        """验证数字的加法运算"""
        actualValue = self.mm.jia(2, 3)
        expectValue = 5
        # 断言
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_add_2(self):
        """验证字符串的拼接运算"""
        actualValue = self.mm.jia("abc", "def")
        expectValue = "abcdef"
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_jian_1(self):
        """验证数字的减法运算"""
        actualValue = self.mm.jian(3, 2)
        expectValue = 1
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_cheng_1(self):
        """验证数字的乘法运算"""
        actualValue = self.mm.chengfa(2, 3)
        expectValue = 6
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_cheng_2(self):
        """验证数字和字符串的乘法运算"""
        actualValue = self.mm.chengfa("a", 2)
        expectValue = "aa"
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_chu_1(self):
        """验证数字的除法运算"""
        actualValue = self.mm.chufa(4, 2)
        expectValue = 2
        self.assertEqual(actualValue, expectValue, "预期结果和实际不一致")

    def test_chu_2(self):
        """验证数字和零的除法运算"""
        actualValue = self.mm.chufa(4, 0)
        expectValue = "error"
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