import pytest

class Test_008:
    # @pytest.mark.skipif(2>1, reason='乐意')
    # @pytest.mark.skipif()
    @pytest.mark.skipif(reason='跳过')
    def test_008_1(self):
        print('---->test_008_1')

    def test_008_2(self):
        print('test_008_2')
