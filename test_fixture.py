import pytest

# 调用方式一,也可以把fixture放到conftest.py里面；
print("**************调用方式一***********************")


# @pytest.fixture(scope="function")
# def login():
#     print("\n前置条件，登录成功！！！")

def test_1(login):
    print("\n需要提取登录，方可执行测试用例！！")


def test_2():
    print("\n不需要登录，就可以直接运行！！")


print("**************调用方式二***********************")


# @pytest.fixture()
# def login2():
#     print("前提条件，数据库连接成功！！")

@pytest.mark.usefixtures("login", "login2")
def test_3():
    print("\n第二种调用方式，运行测试用例；")


print("**************调用方式三***********************")


# @pytest.fixture(autouse=True)
# def login3():
#     print("\n****所有方法都会执行，aoto*****")

@pytest.mark.usefixtures("login2")
def test_4():
    print(123)


# 不是以test开头，加入装饰器也不会执行fixture
@pytest.mark.usefixtures("login2")
def loginss():
    print(123)


if __name__ == "__main__":
    pytest.main(["-vs", "test_fixture.py"])
