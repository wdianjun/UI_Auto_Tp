import allure
import pytest

from utils import DriverUtils

@pytest.mark.run(order=99)
@allure.feature("浏览器环境管理")
class TestEnd:

    @allure.title("关闭浏览器环境")
    def test_end(self):
        with allure.step("关闭浏览器"):
            DriverUtils.set_kd_key(True)
            DriverUtils.quit_kd_drive()
