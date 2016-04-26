# encoding: utf-8

from validtype import *


class Validate(object):
    def __init__(self):
        self._rules = {
            'regular': Regular(),
            'required': Required(),
            'int': Int(),
            'number': Number(),
            'string': String(),
            'email': Email(),
            'mobile': Mobile(),
            'phone': Phone(),
            'url': Url(),
        }

    def is_valid(self, value, rule_dict):
        """
        是否验证通过
        @param rule_dict 验证规则，键为规则名称，值为字典
        @param value 值
        @return True验证通过，False验证失败
        """
        if not rule_dict:
            # 默认验证必填
            rule_dict = {
                'name': 'required',
                'value': None
            }
        rule_name = rule_dict['name']
        rule_value = None
        if 'value' in rule_dict:
            rule_value = rule_dict['value']
        if rule_name not in self._rules:
            raise Exception(u'不支持的验证类型：%s' % rule_name)
        rule = self._rules[rule_name]
        return rule.is_valid(value, rule_value)

    def get_error_msg(self, rule_name):
        if rule_name not in self._rules:
            raise Exception(u'不支持的验证类型：%s' % rule_name)
        rule = self._rules[rule_name]
        return rule.error_msg


class ValidateParam(Validate):
    def __init__(self):
        super(ValidateParam, self).__init__()

    def is_required(self, value):
        return self.is_valid(value, {'name': 'required'})

    def is_int(self, value):
        return self.is_valid(value, {'name': 'int'})

    def is_number(self, value):
        return self.is_valid(value, {'name': 'number'})


class ValidateForm(Validate):
    def __init__(self):
        super(ValidateForm, self).__init__()
        self.__error_dict = {}

    def is_valid(self, param_dict, rule_config_dict):
        """
        是否为有效表单
        @param param_dict: 参数字典，包含名称和值，如django的POST，query_dict对象
        @param rule_config_dict: 表单配置。如：{'name': 'required', 'password': 'string[6,10]'} 密码为6-10位字符串
        @return: True验证通过，False验证失败，错误信息dict
        """
        rtn_is_valid = True
        self.__error_dict.clear()
        for key in param_dict:
            value = param_dict[key]
            rule_name = ''
            if rule_config_dict and key in rule_config_dict:
                rule_name = rule_config_dict[key]
            if rule_name:
                # 解析值范围
                rule_name, min_value, max_value = self.parse_rule_range(rule_name)
                rule_dict = {'name': rule_name, 'value': {'min_value': min_value, 'max_value': max_value}}
                is_valid = super().is_valid(value, rule_dict)
                if not is_valid:
                    rtn_is_valid = False
                    self.__error_dict[key] = self.get_error_msg(rule_name)
        return rtn_is_valid, self.__error_dict

    def parse_rule_range(self, rule_name):
        min_value = 0
        max_value = 65535
        if rule_name:
            range_l = re.findall('^(\w*)\[(\d+[ ]?,[ ]?\d+)\]$', rule_name)
            if range_l:
                rule_name = range_l[0][0]
                range_a = range_l[0][1].split(',')
                min_value = int(range_a[0])
                max_value = int(range_a[1])
        return rule_name, min_value, max_value


if __name__ == '__main__':
    form = ValidateForm()
    print(form.parse_rule_range('string[10, 20]'))





