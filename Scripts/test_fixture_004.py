import pytest

@pytest.fixture(name='login_out')
def bofore_out():
    print('---->ccccc')

@pytest.mark.usefixtures('login_out')
class Test_004:
    # @pytest.fixture()
    # def before_in(self):
    #     print('---->bbbbb')

    def test_004_1(self):
        print('---->aaaaa')
        assert True



