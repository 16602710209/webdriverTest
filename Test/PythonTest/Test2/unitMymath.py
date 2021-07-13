import unittest
import myMath

#  创建一个单元测试类
class unitMymath(unittest.TestCase):
    # 一种注释，在python、java语言中使用这种方式给方法指定了特定的含义
    @classmethod
    def setUpClass(cls):
        print("我是setUpClass方法")
    @classmethod
    def tearDownClass(cls):
        print("我是tearDownClass方法")

    #  方法名不能改，self参数不能少
    def setUp(self):
        self.mm = myMath.mymath()
        print("我是setUp方法")

    #  必须是test开头的方法，这一个就是测试用例
    def test_add_1(self):
        print("我是第一条测试用例")
        # mm = myMath.mymath()
        actualValue = self.mm.jia(10, 12)
        expectValue = 22
        self.assertEqual(actualValue, expectValue, "预期结果和实际不相等")

    def test_add_2(self):
        print("我是第二条测试用例")
        # mm = myMath.mymath()
        actualValue = self.mm.jia("abc", "123")
        expectValue = "abc123"
        self.assertEqual(actualValue, expectValue, "预期结果和实际不相等")

    def test_chengfa_1(self):
        print("我是第三条测试用例")
        actualValue = self.mm.chengfa(12, 2)
        expectValue = 24
        self.assertEqual(actualValue, expectValue, "预期结果和实际不相等")

    #  方法名不能改，self参数不能少
    def tearDown(self):
        print("我是tearDown方法")

if __name__ == "__main__":
    # 调用执行单元测试，通过主方法main执行
    # 这个方法是可以执行我们单元测试用例的，是全部的测试类中全部的测试用例
    # 如果我们只想执行家法运算的单元测试用例呢
    # unittest.main()

    # 方式一、
    suitt2 = unittest.TestSuite()
    # 测试集合对象中有一个方法，addtest-->追加测试用例到测试集合
    # 格式：类名（用例名）
    suitt2.addTest(unitMymath("test_chengfa_1"))
    suitt2.addTest(unitMymath("test_add_1"))
    suitt2.addTest(unitMymath("test_add_2"))

    # 测试集合对象还有一个方法，addtests-->追加多个测试你用例到测试集合
    suitt2.addTests(map(unitMymath, ["test_add_2", "test_add_1"]))

    # 方式二、
    # 可以unittest中提供的testloader模块，提供了好多帮我们把测试用例加载到测试集合中的方法
    # 创建testloader的对象
    loader = unittest.TestLoader()
    # loaderTestsFromName：通过添加一个模块名、类名、测试用例名、将其中的用例直接加载到测试集合
    suitt1 = loader.loadTestsFromName("unitMymath")
    suitt1 = loader.loadTestsFromName("unitMymath.unitMymath.test_add_1")

    # 方法三、
    # 使用TestLoader对象中discover方法加载用例
    # 第一个参数是一个目录，这个目录下可以有单元测试的文件（.py）
    suitt = unittest.defaultTestLoader.discover(r"./", pattern="unitMymath.py")
    print(suitt.countTestCases())

    re = unittest.TestResult()
    suitt.run(re)
    suitt1.run(re)
    suitt2.run(re)


    print(re.__dict__)
