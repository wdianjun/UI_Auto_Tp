import allure
import pytest

from utils import DriverUtils

# 测试用例排序
# 值越小优先级越高，只限整数
@pytest.mark.run(order=1)
@allure.feature("浏览器环境管理")
class TestBegin:

    @allure.title("初始化浏览器环境")
    def test_begin(self):
        with allure.step("设置浏览器暂不关闭"):
            # 运行时修改开关的值为 False
            DriverUtils.set_kd_key(False)
