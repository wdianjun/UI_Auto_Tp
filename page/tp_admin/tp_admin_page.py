
from base.base_page import KdBasePage
from selenium.webdriver.common.by import By
# PO模式
# 后台登录页面
# 继承基类
class AdminLoginPage(KdBasePage):
  # 实例属性-管理操作步骤在该页面中所用到元素定位信息
  def __init__(self):
    super().__init__()
    # 用户名输入框
    self.username = (By.NAME,"username")
    # 密码输入框
    self.password = (By.NAME,"password")
    # 验证码输入框
    self.code = (By.ID,"vertify")
    # 登录按钮
    self.login_btn = (By.NAME,"submit")
    
    
    
  # 实例方法（业务操作层）- 封装测试用例在该页面的操作步骤
  def admin_login(self,usr,pwd,cod):
    # 输入用户名
    self.input_text(element = self.find_el(self.username),text = usr)
    # 输入密码
    self.input_text(element = self.find_el(self.password),text = pwd)
    # 输入验证码
    self.input_text(element = self.find_el(self.code),text = cod)
    # 点击登录按钮
    self.find_el(self.login_btn).click()
    