import pytest


@pytest.fixture(scope="session")
def init_session():
    print("---全局前置")
    yield
    print("---全局后置")


@pytest.fixture(scope="module")
def init_module():
    print("---模块前置")
    yield
    print("---模块后置")


@pytest.fixture(scope="class")
def init_class():
    print("---类前置")
    yield
    print("---类后置")


@pytest.fixture(scope="function")
def init_function():
    print("---方法前置")
    a = "这是一个前置参数"
    yield a
    print("---方法后置")
