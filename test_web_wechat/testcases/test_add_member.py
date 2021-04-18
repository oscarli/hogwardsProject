from test_web_wechat.page.main_page import MainPage
from test_web_wechat.page.add_member import AddMemberPage

class TestAddMember:
    """
    write test case.
    """
    def test_add_member(self):
        main_page = MainPage()
        main_page.goto_add_member().add_member().get_contact_list()