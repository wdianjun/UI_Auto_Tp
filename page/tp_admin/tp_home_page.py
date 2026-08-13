# 后台系统主页
from base.base_page import AdminBasePage


class AdminHomePage(AdminBasePage):
    # 实例属性-管理操作步骤在该页面中所用到元素定位信息
    def __init__(self):
        super().__init__()