import pytest

@pytest.fixture()
def bofore_out(self):
    print('---->ccccc')

class Test_003:
    @pytest.fixture()
    def before_in(self):
        print('---->bbbbb')

    def test_003_1(self,before_in,before_out):
        print('---->aaaaa')
        assert True



