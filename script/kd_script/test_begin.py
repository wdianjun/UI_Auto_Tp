import pytest

from utils import DriverUtils

# 测试用例排序
# 值越小优先级越高，只限整数
@ pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        # 修改关闭浏览器驱动对象的值
        # 运行时修改开关的值为false
        DriverUtils.set_kd_key(False)
