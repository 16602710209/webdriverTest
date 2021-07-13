import pytest


testdata = [{"username": "用户2", "password": "密码2"}, {"username": "用户3", "password": "密码3"}]


@pytest.mark.usefixtures("init_class")
class TestCase():
    @pytest.mark.parametrize('testdata', testdata)
    @pytest.mark.usefixtures("init_function")
    def test_case_01(self, testdata):
        """
        用例一：xxx
        """
        print("输入用户名：{}".format(testdata["username"]))
        print("输入密码：{}".format(testdata["password"]))
        assert 1 == 1
