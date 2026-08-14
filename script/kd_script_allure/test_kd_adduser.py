import time

import allure
import pytest

from page.kd_home_page import KdHomePage
from page.kd_user_page import KdUserPage
from utils import DriverUtils

@pytest.mark.run(order=3)
@allure.feature("用户管理模块")
# 定义测试类
class TestAddUser:
    # 类级别的初始化方法
    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_kd_driver()
        # 打开测试网址
        self.driver.get("https://kdtx-test.itheima.net/")

    # 类级别的销毁方法
    def teardown_class(self):
        # 关闭浏览器
        DriverUtils.quit_kd_drive()

    # 定义测试方法
    @allure.title("新增用户成功")
    def test_add_user(self):
        with allure.step("进入用户管理页面"):
            KdHomePage().kd_home()

        # 每次生成不同的用户名称，避免重复
        username = f"add_{time.strftime('%Y%m%d%H%M%S')}"
        nickname = "测试kdUI"

        with allure.step("填写用户信息并提交"):
            success_message = KdUserPage().kd_add_user(nickname, username)

        with allure.step("断言用户新增成功"):
            try:
                assert "成功" in success_message, (
                    f"新增用户失败，页面提示：{success_message!r}"
                )
            except AssertionError:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name="新增用户失败截图",
                    attachment_type=allure.attachment_type.PNG
                )
                raise
    # def test_add_user(self):
    #   # 执行登录操作步骤
    #   KdLoginPage().kd_login("admin","HM_2023_test","2")
    #   # 执行跳转用户管理页面
    #   KdHomePage().kd_home()
    #   # 执行添加用户操作
    #   # KdUserPage().kd_add_user(f"add_{time.strftime(%Y%m%d%H%M%S%)}","测试kdUI","nick测试UI")
    #   KdUserPage().kd_add_user("测试kdUI","nick测试UI")
    #   time.sleep(5)
    #   # 断言
