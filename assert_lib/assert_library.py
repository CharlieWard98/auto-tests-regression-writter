import assert_lib
import unittest

def assertEqual(first, second, uid, message):
    result = first == second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertEqual(first, second, msg=message)

def assertTrue(first, uid, message):
    result = first == True
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertTrue(first, msg=message)

def assertFalse(first, uid, message):
    result = first == False
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertFalse(first, msg=message)

def assertIn(first, second, uid, message):
    result = first in second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertIn(first, second, msg=message)

def assertNotIn(first, second, uid, message):
    result = first not in second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertNotIn(first, second, msg=message)

def assertGreater(first, second, uid, message):
    result = first > second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertGreater(first, second, msg=message)

def assertGreaterEqual(first, second, uid, message):
    result = first >= second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertGreaterEqual(first, second, msg=message)

def assertLess(first, second, uid, message):
    result = first < second
    assert_lib.reg_sheet.write_test_result(reg_uid=uid, result=result, message=message)
    unittest.TestCase().assertLess(first, second, msg=message)

def assertListEqual(first, second, uid, message):
    assertEqual(first, second, uid, message)




