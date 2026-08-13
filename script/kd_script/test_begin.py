from utils import DriverUtils


class TestBegin:

    def test_begin(self):
        # 修改关闭浏览器驱动对象的值
        # 运行时修改开关的值为false
        DriverUtils.set_kd_key(False)
