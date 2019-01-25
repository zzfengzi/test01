import pytest

class Test_005:
    # 初始化 driver
    def setup_class(self):
        print('---->setup_class')

    def teardown_class(self):
        print('---->teardown_class')

    @pytest.mark.usefixtures('inx')
    def test_005_1(self):
        # 定位元素
        print('---->test_005_1')
        assert True

    @pytest.fixture(name='inx')
    def bofore_in(self):
        print('---->bofore_in')

