import pytest


@pytest.fixture(scope="function")
def login():
    print("\n前置条件，登录成功！！！")


@pytest.fixture()
def login2():
    print("前提条件，数据库连接成功！！")


@pytest.fixture(autouse=True)
def login3():
    print("\n****所有方法都会执行，aoto*****")
