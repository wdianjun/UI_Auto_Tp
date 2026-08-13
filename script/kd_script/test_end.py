import pytest

from utils import DriverUtils

@ pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 修改关闭浏览器驱动对象的值
        # 运行时修改开关的值为Ture
        DriverUtils.set_kd_key(True)
        # 主动关闭浏览器
        DriverUtils.quit_kd_drive()
