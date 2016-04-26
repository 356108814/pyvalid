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

    def test_int(self):
        self.assertEqual(self.int.is_valid('109099-'), False)
        self.assertEqual(self.int.is_valid(12.5), False)
        self.assertEqual(self.int.is_valid('a1'), False)
        self.assertEqual(self.int.is_valid('12.'), False)
        self.assertEqual(self.int.is_valid('-a'), False)

    def test_number(self):
        self.assertEqual(self.number.is_valid('109099-'), False)
        self.assertEqual(self.number.is_valid(12.5), True)
        self.assertEqual(self.number.is_valid('22.'), False)
        self.assertEqual(self.number.is_valid('-778'), True)
        self.assertEqual(self.number.is_valid('+12.6'), False)
        self.assertEqual(self.number.is_valid('哈哈'), False)

    def test_string(self):
        self.assertEqual(self.string.is_valid('109099-', 10), False)
        self.assertEqual(self.string.is_valid(12.5, 1), True)
        self.assertEqual(self.string.is_valid('22.', 5), False)
        self.assertEqual(self.string.is_valid('-778'), True)
        self.assertEqual(self.string.is_valid('+12.6'), True)
        self.assertEqual(self.string.is_valid('哈哈'), True)

    def test_email(self):
        self.assertEqual(self.email.is_valid('asdjfjs@1.com'), True)
        self.assertEqual(self.email.is_valid('asd.jfjs@1..com'), False)

    def test_mobile(self):
        self.assertEqual(self.mobile.is_valid('20012345678'), False)
        self.assertEqual(self.mobile.is_valid('17112345698'), True)

    def test_phone(self):
        self.assertEqual(self.phone.is_valid('021-12345678-1'), True)
        self.assertEqual(self.phone.is_valid('0556-2312584'), True)
        self.assertEqual(self.phone.is_valid('02112345678'), True)
        self.assertEqual(self.phone.is_valid('05562312584'), True)

    def test_url(self):
        self.assertEqual(self.url.is_valid('021-12345678-1'), False)
        self.assertEqual(self.url.is_valid('ww.baidu.com'), True)
        self.assertEqual(self.url.is_valid('http://1.net/a/com/'), True)
        self.assertEqual(self.url.is_valid('05562312584'), False)

if __name__ == '__main__':
    unittest.main()
