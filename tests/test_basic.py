import unittest
from assert_lib.assert_library import *


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        reg_uid = 'REG_001'
        foo_to_upper = 'foo'.upper()
        upper_foo = 'FOO'

        assertEqual(foo_to_upper, upper_foo, reg_uid, f'{foo_to_upper} should equal {upper_foo}')

    def test_isupper(self):
        reg_uid = 'REG_002'
        
        lower_foo = 'Foo'
        upper_foo = 'FOO'

        assertTrue('Foo'.isupper(), reg_uid, f'{lower_foo} should be upper case')
        assertTrue('FOO'.isupper(), reg_uid, f'{upper_foo} should be upper case')

    def test_split(self):
        reg_uid = 'REG_003'

        s = 'hello world'
        expected_split = ['hello', 'world']
        assertEqual(s.split(), ['hello', 'world'], reg_uid, f'{s} split should be {expected_split}')
        
