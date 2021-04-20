import pytest

from test_web_wechat_04.page.main_page import MainPage


class TestAddMember:
    """
    编写测试用例
    """

    def setup_class(self):
        self.main_page = MainPage()

    def teardown_class(self):
        pass
        # self.main_page.quit()

    # 1. 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, accid, phone", [("伊泽瑞尔11", "00901", "13344445525")])
    def test_add_member(self, username, accid, phone):
        # 1. 跳转到添加成员页面  2. 添加成员   3. 获取成员列表
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        print(name_list)
        assert username in name_list

    @pytest.mark.parametrize("username, accid, phone", [("伊泽瑞尔1", "00901", "13344445555")])
    def test_add_member_fail(self, username, accid, phone):
        data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
        err = [i for i in data_list if i != ""]
        assert "伊泽瑞尔" in err[0]

    def test_xxx(self):
        main_page = MainPage()
        main_page.goto_add_member().add_xxx().add_member()
