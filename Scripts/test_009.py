import pytest

class Test_009:
    @pytest.mark.parametrize('a,b',[(1,3),(2,3),(4,0)])
    def test_009_2(self,a, b):
        # a+b = 4
        print('a',a)
        print('b',b)
        assert a+b == 4