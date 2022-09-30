import pytest
from main import YD_user
from parameterized import parameterized

#добавить токен для ЯндексДиска
token_YD = ''

test_param =['Папка_1', 'Папка_2', 'Папка_1']

class TestFuncion:
    @pytest.mark.parametrize('dir_name',test_param)      
    def test_add_directory(self, dir_name):
        inst = YD_user(token_YD)
        name_dir = dir_name
        result = 201
        res = inst.add_directory(name_dir)
        assert result==res
        
    
    
if __name__ == "__main__":
    pytest.main()