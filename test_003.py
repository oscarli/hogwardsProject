"""
@author: Oscar
@time: 2021/4/9 17:57
@file: test_003.py
@desc: 
"""
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, 1)


if __name__ == '__main__':
    unittest.main()
