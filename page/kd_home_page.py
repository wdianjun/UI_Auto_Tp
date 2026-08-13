
from base.base_page import KdBasePage
from selenium.webdriver.common.by import By
# PO模式
# kd首页
# 继承基类
class KdHomePage(KdBasePage):
  # 实例属性-管理操作步骤在该页面中所用到元素定位信息
  def __init__(self):
    super().__init__()
    # 一级系统管理
    self.kd_system = (By.XPATH,"//span[normalize-space()='系统管理']")
    # 二级权限管理
    self.kd_authority = (By.XPATH,"//span[normalize-space()='权限管理']")
    # 三级用户管理
    self.kd_customer = (By.XPATH,"//span[normalize-space()='用户管理']")


  # 实例方法（业务操作层）- 封装测试用例在该页面的操作步骤
  def kd_home(self):
    # 点击一级系统管理
    self.find_el(self.kd_system).click()
    # 点击二级权限管理
    self.find_el(self.kd_authority).click()
    # 点击三级用户管理
    self.find_el(self.kd_customer).click()