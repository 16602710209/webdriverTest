import unittest
import myMath


class unitMymath2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
         print("我是setUpClass方法")

    @classmethod
    def tearDownClass(cls):
        print("我是tearDownClass方法")

    def setUp(self):
        self.mm = myMath.mymath()
        print("我是setUp方法")

    def test_add_1(self):
        actualValue = self.mm.jia(2, 3)
        expectValue = 5
        self.assertEqual(actualValue, expectValue, "预期结果和实际不相等")
        aa = None
        self.assertIsNotNone(aa)
        print("我是第1个测试方法")

    def test_add_2(self):
        print("我是第2个测试")
        actualValue = self.mm.jia("你", "好")
        expectValue = "你好"
        self.assertEqual(actualValue, expectValue, "预期结果和实际结果不相等")
    def test_chengfa_1(self):
        print("我是第3个测试")
        actualValue = self.mm.chengfa(2, 12)
        expectValue = 24
        self.assertEqual(actualValue, expectValue, "预期结果和实际结果不相等")

    def tearDown(self):
        print("我是tearDown方法")

if __name__ == "__main__":

    # # unittest.main()
    # # 创建测试集合
    suitt = unittest.TestSuite()
    # # 使用TestLoader中的discover方法返回测试集合
    suitt = unittest.defaultTestLoader.discover(r"./", pattern="unit*.py")

    # 方法一、
    # # 调用测试集合的run()方法运行测试用例
    # result = unittest.TestResult()
    # suitt.run(result)
    # # 查看结果
    # print(result.__dict__)


    # 方法二、
    # 使用TextTestRunner()运行器提供的run()方法运行测试集合
    # 如何产生一个文件流对象，如果打开一个文本文件，想着往里写入数据
    # 报告是以TextTestresult的形式展示的
    # TextTestRunner是TestRunner的子类
    # TextTestResult是TestResult的子类
    with open(r"./re.txt", "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(f, descriptions="单元测试报告执行", verbosity=2)
        runner.run(suitt)