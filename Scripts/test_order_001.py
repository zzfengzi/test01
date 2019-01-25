import pytest

class Test_order_001:
    @pytest.mark.run(order=1)
    def test_o_002(self):
        print('登录')
        print('---->test_o_002')

    @pytest.mark.run(order=2)
    def test_o_001(self):
        print('设置')
        print('---->test_o_001')

    @pytest.mark.run(order=3)
    def test_o_004(self):
        print('登录')
        print('---->test_o_004')

    @pytest.mark.run(order=4)
    def test_o_005(self):
        print('设置')
        print('---->test_o_005')

