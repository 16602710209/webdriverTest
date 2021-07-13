import pytest


def setup_module():
    print("---模块级别的前置")


def teardown_module():
    print("---模块级别的后置")


def setup_function():
    print("---函数级别的前置")


def teardown_function():
    print("---函数级别的后置")


# class TestCase():
def test_case_01():
    """
    用例一：1+1=2
    """
    n = 1 + 1
    print("相加后的结果：{}".format(n))
    assert n == 2, "断言失败"


def test_case_02():
    m = 2 + 2
    print("相加后的结果：{}".format(m))
    assert m == 4, "断言失败"
