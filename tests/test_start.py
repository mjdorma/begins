from __future__ import absolute_import, division, print_function
import atexit
import mock

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import begin


class TestStart(unittest.TestCase):

    def test_start_false(self):
        # begin.start() return false outside __main__
        self.assertFalse(begin.start())

    def test_start_true(self):
        # mock globals to mimic __main__
        try:
            original = globals()['__name__']
            globals()['__name__'] = "__main__"
            self.assertTrue(begin.start())
        finally:
            globals()['__name__'] = original

    @mock.patch('atexit.register')
    def test_decorate_false(self, register):
        @begin.start
        def main():
            pass
        self.assertEqual(0, register.call_count)


if __name__ == '__main__':
    unittest.begin()
