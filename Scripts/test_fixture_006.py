import pytest

class Test_006:
    @pytest.fixture(scope='class',autouse=True)
    def before_in(self):
        print('---->before_in')

    def test_006_1(self):
        print('---->test_006_1')
        pass

    def test_006_2(self):
        print('---->test_006_2')
        pass










