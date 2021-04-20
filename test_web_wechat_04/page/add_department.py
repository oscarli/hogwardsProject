from selenium.webdriver.common.by import By
from test_web_wechat_04.page.base_page import BasePage


class AddDepartmentPage(BasePage):
    __department_name = (By.CSS_SELECTOR, ".ww_inputText:nth-child(2)")
    __choice = (By.CSS_SELECTOR, ".js_parent_party_name")
    __department = (By.CSS_SELECTOR, ".ww_dialog_body .jstree-anchor")
    __confirm = (By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue")

    def add_department(self, department_name):
        from test_web_wechat_04.page.contact import ContactPage
        self.find(self.__department_name).send_keys(department_name)  # 输入部门
        self.find(self.__choice).click()  # 选择所属部门
        self.find(self.__department).click()
        self.find(self.__confirm).click()  # 点击确定
        return ContactPage(self.driver)

    # def add_department_2(self, department):
    #     # 输入部门
    #     self.wait_for_see((By.CSS_SELECTOR, '.form>div:nth-child(1)>input')).send_keys(department)
    #
    #     # 选择所属部门
    #     self.wait_for_click((By.CSS_SELECTOR, '.js_toggle_party_list'))
    #     self.wait_for_click((By.CSS_SELECTOR, '.js_party_list_container'))
    #
    #     # 点击确定
    #     self.wait_for_click((By.CSS_SELECTOR, '.member_tag_dialog>.qui_dialog_foot>a:nth-child(1)'))
    #     return ContactPage(self.driver)

