import time

from config import BASE_DIR
from page.kd_login_page import KdLoginPage
from utils import DriverUtils, el_is_exist_by_text


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
  def test_login(self):
    # 执行登录操作步骤
    KdLoginPage().kd_login("admin","HM_2023_test","2")
    # time.sleep(5)
    # 断言
    try:
      assert el_is_exist_by_text(self.driver,False,"首页")
    except Exception as e:
      # 截图放在img目录
      self.driver.get_screenshot_as_file(BASE_DIR + "/img/login_failed.png")
      # 继续抛出
      raise e
