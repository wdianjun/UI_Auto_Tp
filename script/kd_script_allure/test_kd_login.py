import allure
import pytest

from page.kd_login_page import KdLoginPage
from utils import DriverUtils, el_is_exist_by_text

@pytest.mark.run(order=2)
@allure.feature("客达天下登录模块")
# 定义测试类
class TestLogin:
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
  @allure.title("登录成功")
  def test_login(self):
    with allure.step("输入账号、密码和验证码并登录"):
      KdLoginPage().kd_login("admin", "HM_2023_test", "2")

    with allure.step("断言登录成功"):
      try:
        assert el_is_exist_by_text(self.driver, False, "首页")
      except AssertionError:
        allure.attach(
          self.driver.get_screenshot_as_png(),
          name="登录失败截图",
          attachment_type=allure.attachment_type.PNG
        )
        raise
