
from selenium.webdriver.common.by import By

from test_web_wechat_04.page.base_page import BasePage
from test_web_wechat_04.page.contact import ContactPage


class AddMemberPage(BasePage):
    # 设定为元祖
    # 页面元素不需要让 业务用例了解，所以要加私有
    __ele_username = (By.ID, "username")
    ele_accid = (By.ID, "memberAdd_acctid")
    ele_phone = (By.ID, "memberAdd_phone")

    def add_member(self, username, accid, phone):
        # * 的作用是 解元祖 self.driver.find_element(*username) 等同于
        # self.driver.find_element(By.ID, "username")

        # self.driver.find_element(*self.__ele_username).send_keys(username)
        self.find(self.__ele_username).send_keys(username)
        self.driver.find_element(*self.ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # 页面的return 分成两个部分
        # 1. 其他页面的 实例
        # 2. 用例所需要的断言
        # 注意： 不要写成 ContactPage
        # 快捷导入  alt + 回车
        return ContactPage(self.driver)

    def add_member_fail(self, username, accid, phone):
        self.driver.find_element(*self.__ele_username).send_keys(username)
        self.driver.find_element(*self.ele_accid).send_keys(accid)
        self.driver.find_element(*self.ele_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        element = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = []
        for ele in element:
            error_list.append(ele.text)
        return error_list

    def add_xxx(self):

        # 调用本身的实例
        # AddMemberPage()
        return self
