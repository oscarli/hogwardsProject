import itertools
import pytest
from test_web_wechat_04.page.main_page import MainPage


@pytest.fixture()
def main_page():
    main = MainPage()
    yield main
    main.driver.quit()


# 实现ids中可以显示中文
def pytest_collection_modifyitems(items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# # 实现ids中可以显示中文
# def pytest_collection_modifyitems(session, config, items: list) -> None:
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# # 初始化用例与释放用例
# @pytest.fixture(scope="session")
# def get_init():
#     main = MainPage()
#     yield main
#     main.driver.quit()


# # fixture实现笛卡尔积参数化
# @pytest.fixture(params=[element for element in itertools.product(*get_AddMenmberData())])
# def get_addData(request):
#     return request.param
#
#
# @pytest.fixture(params=get_AddDepartment()[0], ids=get_AddDepartment()[1])
# def get_addDepartment(request):
#     return request.param
