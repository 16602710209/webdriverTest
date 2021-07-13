import pytest


@pytest.mark.usefixtures('init_class')
class TestCase():

    def test_case_01(self):
        """
        用例一：1+1=2
        """
        n = 1 + 1
        print("相加后的结果：{}".format(n))
        assert n == 2, "断言失败"

    @pytest.mark.usefixtures('init_function')
    def test_case_02(self, init_function):
        m = 2 + 2
        print(init_function)
        print("相加后的结果：{}".format(m))
        assert m == 4, "断言失败"
