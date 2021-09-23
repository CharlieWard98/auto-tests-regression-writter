import unittest

if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover('tests')
    results = unittest.TextTestRunner(verbosity=2).run(tests)