# encoding: utf-8

import unittest
from validtype import *


class TestValidType(unittest.TestCase):
    def setUp(self):
        self.int = Int()
        self.number = Number()
        self.string = String()
        self.email = Email()
        self.mobile = Mobile()
        self.phone = Phone()
        self.url = Url()

    def tearDown(self):
        pass

    # def test_int(self):
    #     print(self.int.is_valid('109099-'))
    #     print(self.int.is_valid(12.5))
    #     print(self.int.is_valid('a1'))
    #     print(self.int.is_valid('12.'))
    #     print(self.int.is_valid('-a'))

    # def test_number(self):
    #     print(self.number.is_valid('109099-'))
    #     print(self.number.is_valid(12.5))
    #     print(self.number.is_valid('22.'))
    #     print(self.number.is_valid('-778'))
    #     print(self.number.is_valid('+12.6'))
    #     print(self.number.is_valid('哈哈'))

    # def test_string(self):
    #     print(self.string.is_valid('109099-', 10))
    #     print(self.string.is_valid(12.5, 1))
    #     print(self.string.is_valid('22.', 5))
    #     print(self.string.is_valid('-778'))
    #     print(self.string.is_valid('+12.6'))
    #     print(self.string.is_valid('哈哈'))

    # def test_string(self):
    #     print(self.email.is_valid('asdjfjs@1.com'))
    #     print(self.email.is_valid('asd.jfjs@1..com'))

    # def test_mobile(self):
    #     print(self.mobile.is_valid('20012345678'))
    #     print(self.mobile.is_valid('17112345698'))

    # def test_phone(self):
    #     print(self.phone.is_valid('021-12345678-1'))
    #     print(self.phone.is_valid('0556-2312584'))
    #     print(self.phone.is_valid('02112345678'))
    #     print(self.phone.is_valid('05562312584'))

    def test_url(self):
        print(self.url.is_valid('021-12345678-1'))
        print(self.url.is_valid('ww.baidu.com'))
        print(self.url.is_valid('http://1.net/a/com/'))
        print(self.url.is_valid('05562312584'))

if __name__ == '__main__':
    unittest.main()
