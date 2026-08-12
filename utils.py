import json
import logging
import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_DIR

# from selenium.webdriver.support import expected_conditions as EC


class DriverUtils:

    # 获取浏览器驱动对象
    # 整个测试用例运行过程中会多次调用获取驱动对象的方法，按照实例方法调用的话每次都要创建对象，调用就会出现多个浏览器
    # 整个测试用例运行时，第一次打开浏览器驱动对象，则把浏览器驱动对象存储起来
    # 下次调用获取驱动对象时，判断当前是否有存储的浏览器驱动对象，如有则直接返回，如没有则创建

    # 门户网站驱动对象存储的私有属性
    __buyer_driver = None
    # 后台管理系统网站驱动对象存储的私有属性
    __admin_driver = None
    # App驱动对象存储的私有属性

    @classmethod
    # 获取门户网站驱动对象
    def get_buyer_driver(cls):
        if cls.__buyer_driver is None:
            service = Service(
                r"/Users/D1anJun/Downloads/test/driver/chromedriver"
            )  # Mac存放浏览器驱动地址
            # service = Service(r"D:\test\driver\chromedriver.exe") # win地址
            cls.__buyer_driver = webdriver.Chrome(service=service)
            # 最大化窗口
            cls.__buyer_driver.maximize_window()
            # 隐式等待
            cls.__buyer_driver.implicitly_wait(10)
        return cls.__buyer_driver

    # 关闭门户网站驱动对象
    @classmethod
    def quit_buyer_drive(cls):
        # 为了加强代码的健壮性，避免单独调用关闭浏览器驱动方法时报警，在调用关闭驱动对象的方法时先判断
        # 当前是否有打开的浏览器
        if cls.__buyer_driver is not None:
            time.sleep(2)
            cls.__buyer_driver.quit()
            # 关闭后要把__driver置空
            cls.__buyer_driver = None

    # 获取后台网站驱动对象
    @classmethod
    def get_admin_driver(cls):
        if cls.__admin_driver is None:
            service = Service(
                r"/Users/D1anJun/Downloads/test/driver/chromedriver"
            )  # Mac存放浏览器驱动地址
            # service = Service(r"D:\test\driver\chromedriver.exe") # win地址
            cls.__admin_driver = webdriver.Chrome(service=service)
            # 最大化窗口
            cls.__admin_driver.maximize_window()
            # 隐式等待
            cls.__admin_driver.implicitly_wait(20)
        return cls.__admin_driver

    # 关闭后台网站驱动对象
    @classmethod
    def quit_admin_drive(cls):
        # 为了加强代码的健壮性，避免单独调用关闭浏览器驱动方法时报警，在调用关闭驱动对象的方法时先判断
        # 当前是否有打开的浏览器
        if cls.__admin_driver is not None:
            time.sleep(2)
            cls.__admin_driver.quit()
            # 关闭后要把__driver置空
            cls.__admin_driver = None


# 函数：获取公共元素的文本(作用：在测试用例执行完毕后，需要获取结果页面指定的元素数据来做断言)
def get_el_text(driver, xpath_str):
    # msg = DriverUtils.get_driver().find_element(By.XPATH,"//*[@class='el-message-box__message']").text
    # 一般获取实际结果最好加上显式等待
    try:
        msg = (
            WebDriverWait(driver, 10, 1)  # 因为有多个平台门户和后台所以把驱动对象作为参数传进来
            .until(lambda x: x.find_element(By.XPATH, xpath_str))
            .text
        )
        print(msg)
    except Exception as e:
        logging.error(f"没有获取到{xpath_str}.的元素对象文本！")
        msg = None
    return msg


# 函数:根据文本判断当前页面是否有对应的元素对象
def el_is_exist_by_text(driver, is_app, key_text):
    """
    driver: 传驱动对象,
    is_app: 是否为app标识,
    key_text: 关键字文本
    """
    if is_app:
        xpath_str = f"//*[@text='{key_text}']"
    else:
        xpath_str = f"//*[text()='{key_text}']"
    # 根据本次新增的联系人信息的文本，到界面上找元素，如能找到则代表新增成功找不到则失败截图
    try:
        # 如找到元素对象则把元素对象赋值给is_suc
        is_suc = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element(By.XPATH, xpath_str))
    except Exception as e:
        # 找不到则给is_suc赋值为False
        is_suc = False
        # 截图
        # driver.get_screenshot_as_file(f"{key_text}未找到.png")
        logging.error(f"未找到文本为{key_text}的元素对象！")
    # 返回是否找到结果
    return is_suc


# 函数：读取测试数据并转换成pytest参数化所要求的数据格式
def read_test_data(file_path):
    # 文件路径
    filepath = BASE_DIR + f"/data/{file_path}.json"
    # 读取测试数据
    with open(file_path, "r", encoding="utf-8") as f:
        test_data = []
        data = json.load(f)
    # 转换成pytest参数化所要求的数据格式
    for i in data:
        i.pop("desc")  # 删除字典中不需要的键值对
        res = tuple(i.values())
        test_data.append(res)
    return test_data
