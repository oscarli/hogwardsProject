from selenium.webdriver.common.by import By

from test_web_wechat_04.page.add_member import AddMemberPage
from test_web_wechat_04.page.base_page import BasePage
from test_web_wechat_04.page.contact import ContactPage


class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """

    __contact_menu = (By.CSS_SELECTOR, "#menu_contacts")
    __add_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(self.__contact_menu).click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 返回要跳转页面的实例对象

        self.find(self.__add_member).click()
        return AddMemberPage(self.driver)
