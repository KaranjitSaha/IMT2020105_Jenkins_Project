#!/usr/bin/python3
# Passed Test case for checking Maximum of numbers

import unittest
from Maximum import Maximum


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(Maximum(42, 24), 42)

    def testCase2(self):
        self.assertEqual(Maximum(69, 96), 96)

    def testCase3(self):
        self.assertEqual(Maximum(67, 23), 67)

    def testcase4(self):
        self.assertEqual(Maximum(51, 41), 51)



if __name__ == '__main__':
    unittest.main()