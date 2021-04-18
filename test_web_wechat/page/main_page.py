from test_web_wechat.page.add_member import AddMemberPage
from test_web_wechat.page.base_page import BasePage


class MainPage(BasePage):
    """
    公共方法
    """
    def goto_contact(self):
        pass

    def goto_add_member(self):
        return AddMemberPage()
