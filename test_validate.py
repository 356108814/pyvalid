# encoding: utf-8

import unittest
from validate import *


class TestValidate(unittest.TestCase):
    def setUp(self):
        self.validate_param = ValidateParam()
        self.validate_form = ValidateForm()

    def tearDown(self):
        pass

    # def test_param(self):
    #     print(self.validate_param.is_required(''))
    #     print(self.validate_param.is_int('-121'))
    #     print(self.validate_param.is_number('1009.00'))
    #     print(self.validate_param.is_number('aa'))

    def test_form(self):
        param_dict = {
            'name': 'dream',
            'age': '17',
            'mobile': '15510213658'
        }
        rule_config_dict = {
            'name': 'string[10,20]',
            'age': 'int',
            'mobile': 'mobile'
        }
        print(self.validate_form.is_valid(param_dict, rule_config_dict))
        # print(self.validate_form.is_int('-121'))

if __name__ == '__main__':
    unittest.main()
