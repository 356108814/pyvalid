# encoding: utf-8

"""
验证类型
@author Yuriseus
@create 2016-5-13 14:59
"""

import re


class Regular(object):
    """自定义正则验证基类"""
    def __init__(self, rule='', error_msg=u'格式不正确', name=None):
        if name:
            self.name = name
        else:
            self.name = self.__class__.__name__.lower()
        self.rule = rule
        self.error_msg = error_msg

    def is_valid(self, value, rule_value=None):
        """
        是否验证通过。子类必须覆盖此方法
        @param value 值
        @param rule_value 规则需要的参数值字典
        @return True验证通过，False验证失败
        """
        return re.compile(self.rule).match(str(value)) is not None

    def valid_range(self, value, rule_value=None):
        """验证数值范围"""
        try:
            float(value)
            is_number = True
        except Exception as e:
            is_number = False
        min_value = 0
        max_value = 65535
        if is_number:
            if rule_value:
                if 'min_value' in rule_value:
                    min_value = rule_value['min_value']
                if 'max_value' in rule_value:
                    max_value = rule_value['max_value']
                if min_value <= float(value) <= max_value:
                    return True
                else:
                    self.error_msg = u'数字必须在{0}和{1}之间'.format(min_value, max_value)
                    return False
            else:
                return True
        else:
            if max_value != 65535:
                self.error_msg = u'数字必须在{0}和{1}之间'.format(min_value, max_value)
            return False


class Required(Regular):
    """必填"""
    def __init__(self):
        super(Required, self).__init__('', u'必填项，不能为空')

    def is_valid(self, value, rule_value=None):
        if value:
            return True
        else:
            return False


class Int(Regular):
    """整数"""
    def __init__(self):
        super(Int, self).__init__('^[-]?[0-9]+$', u'只能输入整数')

    def is_valid(self, value, rule_value=None):
        is_int = re.compile(self.rule).match(str(value)) is not None
        if is_int:
            return self.valid_range(value, rule_value)
        else:
            return False


class Number(Regular):
    """数字"""
    def __init__(self):
        super(Number, self).__init__('^[-]?[0-9]+[.]?[0-9]+$', u'只能输入数字')

    def is_valid(self, value, rule_value=None):
        is_number = re.compile(self.rule).match(str(value)) is not None
        if is_number:
            return self.valid_range(value, rule_value)
        else:
            return False


class String(Regular):
    """指定长度字符串"""
    def __init__(self):
        super(String, self).__init__('', u'字符串长度必须介于{0}到{1}之间')

    def is_valid(self, value, rule_value=None):
        # min_value = 0
        # max_value = 65535
        # if value:
        #     if rule_value:
        #         if 'min_value' in rule_value:
        #             min_value = rule_value['min_value']
        #         if 'max_value' in rule_value:
        #             max_value = rule_value['max_value']
        #         self.error_msg = self.error_msg.format(min_value, max_value)
        #         if min_value <= len(str(value)) <= max_value:
        #             return True
        #         else:
        #             return False
        #     else:
        #         return True
        # else:
        #     return False
        return self.valid_range(len(str(value)), rule_value)


class Email(Regular):
    """邮箱"""
    def __init__(self):
        super(Email, self).__init__('^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]+$', u'邮箱格式不正确')


class Mobile(Regular):
    """手机号"""
    def __init__(self):
        super(Mobile, self).__init__('^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|171|18[0|1|2|3|5|6|7|8|9])\d{8}$',
                                     u'手机号不正确')


class Phone(Regular):
    """电话号码"""
    def __init__(self):
        super(Phone, self).__init__('^\d{3}[-]?\d{8}|\d{4}[-]?\d{7}$', u'电话号码不正确')


class Url(Regular):
    """网址"""
    def __init__(self):
        super(Url, self).__init__('^(\w+:\/\/)?\w+(\.\w+)+.*$', u'url不正确')



