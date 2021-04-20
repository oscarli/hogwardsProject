from selenium.webdriver.common.by import By
from test_web_wechat_04.page.add_department import AddDepartmentPage
from test_web_wechat_04.page.base_page import BasePage


class ContactPage(BasePage):
    __name_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    __add_member = (By.CSS_SELECTOR, ".js_add_member:nth-child(2)")
    __plus_button = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __add_department = (By.CSS_SELECTOR, ".js_create_party")
    __department_list = (By.CSS_SELECTOR, ".jstree-leaf a")

    def get_contact_list(self):
        # 获取的是元素列表
        ele_list = self.finds(self.__name_list)
        name_list = []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        return name_list

    def get_department(self):
        self.driver.refresh()
        departments = self.finds(self.__department_list)
        titlist = [element.text for element in departments]
        return titlist

    def goto_add_member(self):
        from test_web_wechat_04.page.add_member import AddMemberPage
        self.find(self.__add_member).click()
        return AddMemberPage(self.driver)

    def goto_department(self):
        self.find(self.__plus_button).click()
        self.find(self.__add_department).click()
        return AddDepartmentPage(self.driver)


if __name__ == '__main__':
    print(ContactPage().get_contact_list())