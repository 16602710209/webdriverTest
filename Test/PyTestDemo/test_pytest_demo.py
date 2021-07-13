import pytest
class TestCase():
    def setup(self):
        print("---setup自动化测试开始")

    def teardown(self):
        print("---teardown自动化测试结束")
    def test_case_01(self):
        """
        用例一：1+1=2
        """
        n = 1+1
        print("相加后的结果：{}".format(n))
        assert n == 2, "断言失败"

    def test_case_02(self):
        m = 2+2
        print("相加后的结果：".format(m))
        assert m == 4, "断言失败"
