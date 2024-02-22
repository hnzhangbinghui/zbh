import pytest

# @pytest.fixture(scope="module")
# def test_addfinalizer(request):
#     print("再次打开浏览器")
#     test="test_addfinalizer"
#     def fin():
#         print("再次关闭浏览器")
#     request.addfinalizer(fin)
#     return test
@pytest.fixture(scope="module")
def test_addfinalizer(request):
    print("再次打开浏览器")
    test="test_addfinalizer"
    yield test
    def fin():
        print("再次关闭浏览器")
    return fin()
def test_anthor(test_addfinalizer):
    print("\n最新用例",test_addfinalizer)

if __name__ == "__main__":
    pytest.main(["-vs", "addfinalizer.py"])






