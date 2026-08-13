import logging

from utils import DriverUtils
from selenium.webdriver.support.ui import WebDriverWait


# 基类：存放二次封装的公共方法，供其他页面对象类继承使用
class BuyerBasePage:
    # 存储驱动对象
    def __init__(self):
        self.driver = DriverUtils.get_buyer_driver()

    # 公用元素定位
    def find_el(self, location):
        # 显式等待
        try:
            res = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*location))
            logging.info(f"成功获取到{location}的元素对象！")
        except Exception as e:
            logging.error(f"没有获取到{location}的元素对象！")
            res = None
        return res

    # 公用模拟输入
    def input_text(self, element, text):
        try:
            element.clear()
            element.send_keys(text)
            logging.info(f"成功在{element}的元素对象中输入{text}！")
        except Exception as e:
            logging.error(f"没有在{element}的元素对象中输入{text}！")

    # frame切换
    def switch_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
            logging.info(f"成功切换到{frame}的iframe中！")
        except Exception as e:
            logging.error(f"没有切换到{frame}的iframe中！")

    # 窗口切换
    def switch_window(self, n):
        try:
            # 获取所有窗口句柄
            handles = self.driver.window_handles
            # 切换到指定窗口
            self.driver.switch_to.window(handles[n])
            logging.info(f"成功切换到{handles[n]}的窗口中！")
        except Exception as e:
            logging.error(f"没有切换到{handles[n]}的窗口中！")


class AdminBasePage:
    # 存储驱动对象
    def __init__(self):
        self.driver = DriverUtils.get_admin_driver()

    # 公用元素定位
    def find_el(self, location):
        # 显式等待
        try:
            res = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*location))
            logging.info(f"成功获取到{location}的元素对象！")
        except Exception as e:
            logging.error(f"没有获取到{location}的元素对象！")
            res = None
        return res

    # 公用模拟输入
    def input_text(self, element, text):
        try:
            element.clear()
            element.send_keys(text)
            logging.info(f"成功在{element}的元素对象中输入{text}！")
        except Exception as e:
            logging.error(f"没有在{element}的元素对象中输入{text}！")

    # frame切换
    def switch_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
            logging.info(f"成功切换到{frame}的iframe中！")
        except Exception as e:
            logging.error(f"没有切换到{frame}的iframe中！")

    # 窗口切换
    def switch_window(self, n):
        try:
            # 获取所有窗口句柄
            handles = self.driver.window_handles
            # 切换到指定窗口
            self.driver.switch_to.window(handles[n])
            logging.info(f"成功切换到{handles[n]}的窗口中！")
        except Exception as e:
            logging.error(f"没有切换到{handles[n]}的窗口中！")



# kd
class KdBasePage:
    # 存储驱动对象
    def __init__(self):
        self.driver = DriverUtils.get_admin_driver()

    # 公用元素定位
    def find_el(self, location):
        # 显式等待
        try:
            res = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*location))
            logging.info(f"成功获取到{location}的元素对象！")
        except Exception as e:
            logging.error(f"没有获取到{location}的元素对象！")
            res = None
        return res

    # 公用模拟输入
    def input_text(self, element, text):
        try:
            element.clear()
            element.send_keys(text)
            logging.info(f"成功在{element}的元素对象中输入{text}！")
        except Exception as e:
            logging.error(f"没有在{element}的元素对象中输入{text}！")

    # frame切换
    def switch_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
            logging.info(f"成功切换到{frame}的iframe中！")
        except Exception as e:
            logging.error(f"没有切换到{frame}的iframe中！")

    # 窗口切换
    def switch_window(self, n):
        try:
            # 获取所有窗口句柄
            handles = self.driver.window_handles
            # 切换到指定窗口
            self.driver.switch_to.window(handles[n])
            logging.info(f"成功切换到{handles[n]}的窗口中！")
        except Exception as e:
            logging.error(f"没有切换到{handles[n]}的窗口中！")


