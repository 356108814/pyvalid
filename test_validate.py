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
        self.assertEqual(self.validate_param.is_required(''), False)
        self.assertEqual(self.validate_param.is_int('-121'), True)
        self.assertEqual(self.validate_param.is_number('1009.00'), True)
        self.assertEqual(self.validate_param.is_number('aa'), False)

    def test_form(self):
        param_dict = {
            'name': 'dream',
            'age': '17',
            'mobile': '155102136d58'
        }
        rule_config_dict = {
            'name': 'string[4,20]',
            'age': 'int',
            'mobile': 'mobile'
        }
        is_valid, error_msg = self.validate_form.is_valid(param_dict, rule_config_dict)
        self.assertEqual(is_valid, False)
        print(error_msg)

if __name__ == '__main__':
    unittest.main()
