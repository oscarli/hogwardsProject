"""
@author: Oscar
@time: 2021/4/15 17:48
@file: test_selenium.py
@desc: 
"""
from time import sleep

import yaml
from selenium import webdriver


class TestDemo:

    def setup(self):
        # Chrome C要大写；
        # 实例化 driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id("su").click()
        ele = self.driver.find_element_by_link_text("霍格沃兹测试学院 – 软件自动化测试开发培训_接口性能测试")
        assert ele


# 复用浏览器
class TestWework:
    def test_wework(self):
        # 复用只支持chrome浏览器
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        # 在当前页面点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 获取cookie信息
        cookies = self.driver.get_cookies()
        # 把cookie存如yaml文件内
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)


def test_cookie():
    # 实例化 driver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853776947167'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853776947167'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3702457'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02701162'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '_F01MVWB0fzgFdbDXPuwQblNwxVLH25rIfMfeUD6NbgnGLfdD8sp9aax6Ug5dM5M'}, {'domain': '.qq.com', 'expiry': 1618577119, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.89481422.1618487420'}, {'domain': 'work.weixin.qq.com', 'expiry': 1618518954, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7q4qho8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1642068084, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/', 'secure': False, 'value': '2249797181056629500%2C391495805822976300%2C2049667375344401700'}, {'domain': '.qq.com', 'expiry': 1642068084, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/', 'secure': False, 'value': '1604902744%2C1608793550%2C1610532084'}, {'domain': '.work.weixin.qq.com', 'expiry': 1624373590, 'httpOnly': False, 'name': '__utmz', 'path': '/', 'secure': False, 'value': '135912439.1608605591.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'}, {'domain': '.qq.com', 'expiry': 1620960294, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1140341230'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640141591, 'httpOnly': False, 'name': 'Hm_lvt_f2ba645ba13636ba52b0234381f51cbc', 'path': '/', 'secure': False, 'value': '1608605591'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1923032785, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'AweDHpNrfZcB0O614dSUcyck3G1krFhbF4da1m2WtsmiOYhLQ0idzFQq5AAIP1tjbeqnv-rdjGq5icIYARNou1p6BAkvkc6Mq6XOkQT3UYC4Yj1y6Ds5RdvOa8-irCGqXFNNI0RcCMY3sDtpOuYqeIYbTEq85p-FPe56TB1qKlfwxonqIgGt7JCi5NjpHO0MrpMSmqQX8tj_NqxQdiKZ2nISZ2Y9_bhISJ3Pd9NzLtnUmC70nybVhsUFjBdcRs_hLchv3pwLViN4K2QIEpfuaA'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650026703, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618321514,1618385974,1618487419,1618490703'}, {'domain': '.qq.com', 'expiry': 1913719559, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1140341230'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621083302, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1681562719, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1623653580.1597756769'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1618490703'}, {'domain': '.work.weixin.qq.com', 'expiry': 1671677590, 'httpOnly': False, 'name': '__utma', 'path': '/', 'secure': False, 'value': '135912439.1623653580.1597756769.1608605591.1608605591.1'}, {'domain': '.qq.com', 'expiry': 1915776880, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '24eb4972699141be'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629292762, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1140341230'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '50fe3df9eb9435ead58c8290282aaf977154534e56811646dbbef3454258458d'}, {'domain': '.qq.com', 'expiry': 1620960294, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000b729cb3eccc57eb59bfbf6f40f7ae08b945a1c97b5247f10302eeff8f43485add60f9f1e57fde423'}, {'domain': '.qq.com', 'expiry': 1640656150, 'httpOnly': True, 'name': '_tc_unionid', 'path': '/', 'secure': False, 'value': '47233a97-f8d6-49d2-90b2-01285a8bb944'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'FhyMDUK2Yb'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325004134706'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6815468544'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1642135485'}]
    # 变量cookies
    for cookie in cookies:
        # 设置cookie
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    sleep(5)


# 使用序列化cookie的方法登录
def test_cookie_v2():
    # 实例化 driver
    driver = webdriver.Chrome()
    # 访问扫码登录页面
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        print(yaml_data)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    sleep(5)



