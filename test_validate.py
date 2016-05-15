# encoding: utf-8

import unittest
from validate import *


class TestValidate(unittest.TestCase):
    def setUp(self):
        self.validate_param = ValidateParam()
        self.validate_form = ValidateForm()

    def tearDown(self):
        pass

    def test_param(self):
        is_valid, error_msg = self.validate_param.is_valid('abc', {'type': 'string', 'min': 1, 'max': 2})
        is_valid, error_msg = self.validate_param.is_valid('a', {'type': 'string', 'required': True})
        print(error_msg)
        self.assertEqual(is_valid, True)

    def test_form(self):
        param_dict = {
            'name': 'dream',
            'age': '17',
            'mobile': '15510213632'
        }
        rule_config_dict = {
            'name': {'type': 'string', 'min': 1, 'max': 5},
            'age': {'type': 'int', 'required': True},
            'mobile': {'type': 'mobile', 'required': True}
        }
        is_valid, error_msg = self.validate_form.is_valid(param_dict, rule_config_dict)
        print(error_msg)
        self.assertEqual(is_valid, True)


if __name__ == '__main__':
    unittest.main()
