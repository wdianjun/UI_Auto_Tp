
from base.base_page import KdBasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# PO模式
# kd首页
# 继承基类
class KdUserPage(KdBasePage):
  # 实例属性-管理操作步骤在该页面中所用到元素定位信息
  def __init__(self):
    super().__init__()
    # 如果是在iframe标签里，需要做frame切换
    # 新增用户
    self.kd_add_user_btn = (By.XPATH,"//span[normalize-space()='新增']")
    # 用户昵称输入框
    self.kd_nickname_input = (By.XPATH,"//input[@placeholder='请输入用户昵称']")
    # 用户名称输入框
    self.kd_username_input = (By.XPATH,"(//input[@placeholder='请输入用户名称'])[2]")
    # 确定按钮
    self.kd_confirm_btn = (
      By.XPATH,
      "//input[@placeholder='请输入用户昵称']"
      "/ancestor::div[contains(concat(' ',normalize-space(@class),' '),' el-dialog ')][1]"
      "//div[contains(concat(' ',normalize-space(@class),' '),' dialog-footer ')]"
      "//button[contains(concat(' ',normalize-space(@class),' '),' cus-search-btn ')]"
    )
    # 新增操作提示（成功或失败）
    self.kd_result_msg = (By.CSS_SELECTOR, ".el-message")


  # 实例方法（业务操作层）- 封装测试用例在该页面的操作步骤
  def kd_add_user(self,nickname,username):
    """
    添加用户
    :param nickname: 用户昵称
    :param username: 用户名称
    """
    # 点击新增用户
    self.find_el(self.kd_add_user_btn).click()
    # 输入用户昵称
    self.input_text(self.find_el(self.kd_nickname_input), nickname)
    # 输入用户名称
    self.input_text(self.find_el(self.kd_username_input), username)
    # 点击确定按钮
    self.find_el(self.kd_confirm_btn).click()
    # 页面可能保留隐藏的历史消息，必须等待本次操作产生的可见消息
    result_msg = WebDriverWait(self.driver, 10, 0.2).until(
      lambda driver: next(
        (element for element in driver.find_elements(*self.kd_result_msg)
         if element.is_displayed() and element.get_attribute("textContent").strip()),
        False
      )
    )
    return result_msg.get_attribute("textContent").strip()
