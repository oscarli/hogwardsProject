import time
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver的实例化
    """

    # 没有参数传入， 会取默认None ,如果有参数传入,会取传入的参数
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver is None:
            # 复用只支持chrome浏览器，命令行需要先启动调试模式：Google\ Chrome --remote-debugging-port=9222
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            # # 实例化 driver
            # self.driver = webdriver.Chrome()
            # # 访问扫码登录页面
            # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            # self.read_and_add_cookies()
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = base_driver
        # 最大化浏览器窗口
        self.driver.maximize_window()
        # 设置隐式等待时间，每一次调用find方法，就会轮询查找元素是否存在
        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()
        print("=======[quit driver succeed!]=======")

    def find(self, by, element=None):
        """
        :param by: 定位方式 css, xpath, id
        :param element: 元素定位信息
        :return:
        """
        # 两种传入定位元素的方式，提高代码的兼容性; 如果传入的是元祖,那就只有一个参数
        if element is None:
            # 比如传入username = (By.ID, "username")
            # * 的作用是解元祖self.driver.find_element(*username) 等同于
            # self.driver.find_element(By.ID, "username")
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, element)

    def finds(self, by, elements=None):
        if elements is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, elements)

    # 获取cookie并写入文件保存
    def get_and_save_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(6)
        with open("../data/cookie.yaml", 'w') as f:
            yaml.dump(self.driver.get_cookies(), f)

    # 清除所有缓存
    def del_cookies(self):
        self.driver.delete_all_cookies()

    # 读取cookies并复用cookies
    def read_and_add_cookies(self):
        with open("../data/cookie.yaml", 'r') as f:
            for cookie in yaml.safe_load(f):
                self.driver.add_cookie(cookie)
        # return self.driver.get(CD()["url"])

    # def cookiesMultiplexing(self):
    #     # 获取当前页的cookies并记录
    #     self.get_and_save_cookies()
    #
    #     # # 清除浏览器cookies
    #     # self.del_cookies()
    #
    #     # 打开网页
    #     self.driver.get(CD()["url"])
    #
    #     # 最大化窗口
    #     self.driver.maximize_window()
    #
    #     # 读取文件中记录的cookies并复用
    #     self.read_and_add_cookies()

    def wait_for_see(self, locate: tuple, timeout: float = 10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locate))
        return element

    def wait_for_click(self, locate: tuple, timeout: float = 15):
        element: WebElement = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locate))
        return element.click()

    def js_click(self, locate: tuple):
        element: WebElement = self.wait_for_see(locate)
        return self.driver.execute_script("$(arguments[0]).click()", element)
    # # 获取下拉框中的所有文本信息
    # def get_dropBox_text(self, locate: tuple):
    #     elements: list = self.finds(*locate)
    #     return elements
    #
    # # 点击下拉框
    # def drop_box_select_elements(self, locate: tuple):
    #     self.wait_for_click(locate)

    # 判断元素是否在下拉框文本中
    def determine_dropBox_text(self, locate: tuple, getLocate: tuple, element):
        # 点击下拉框
        self.wait_for_click(locate)
        if any(element in elements for elements in [el.text for el in self.finds(getLocate)]):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return ActionChains(self.driver).double_click(element).perform()
        else:
            return "未找到该元素"

    # 判断手机号码的地区和需要输入的号码，以形如86-18078844874的字符串传值
    def judge_phone_number(self, dropBox: tuple, dropElements: tuple, locate: tuple, phoneNumber: str):
        """
        :param dropBox: 定位下拉框元素
        :param dropElements: 定位下拉框文本元素
        :param locate: 定义输入框元素
        :param phoneNumber: 电话号码
        :return:
        """
        if "-" in phoneNumber:
            # 点击区号
            self.determine_dropBox_text(dropBox, dropElements, phoneNumber.split("-")[0])
            # 输入电话号码
            self.wait_for_see(locate).send_keys(phoneNumber.split("-")[1])
        else:
            self.wait_for_see(locate).send_keys(phoneNumber)


if __name__ == '__main__':
    BasePage().get_and_save_cookies()
