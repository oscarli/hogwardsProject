from selenium.webdriver.common.by import By

from test_web_wechat.page.base_page import BasePage


class ContactPage(BasePage):
    def get_contact_list(self):
        # 获取的是元素列表
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list)
        name_list = []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        print(name_list)
        return name_list
