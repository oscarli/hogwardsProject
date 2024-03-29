import pytest
from test_web_wechat_04.data.get_data import get_yaml_data


class TestAddDepartment:

    @pytest.mark.parametrize("department_name", get_yaml_data('../data/department.yaml'))
    def test_add_department(self, department_name, main_page):
        dp_name = main_page.goto_contact().goto_add_department().add_department(department_name).get_department()
        assert department_name in dp_name
