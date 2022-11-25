#!/usr/bin/python3
# Failing Test case for Maximum of numbers

import unittest
from Maximum import Maximum


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(Maximum(-5, 2), -5)

    def testCase2(self):
        self.assertEqual(Maximum(69, 23), 23)

    def testCase3(self):
        self.assertEqual(Maximum(0,1), 0)


if __name__ == '__main__':
    unittest.main()