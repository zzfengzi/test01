import pytest

@pytest.fixture(params=['1','2','3'])
def data(request):
    return request.param

class Test_Add:
    @pytest.fixture(scope='class', autouse=True)
    def click_con_list(self): #执行一次
        #点击联系人
        print('11111')

    @pytest.fixture(autouse=True)
    def click_add_con(self): # 执行三次
        #点击
        print('2222')

    def test_add_con(self,data): # 执行三次
        #添加
        print('33333')